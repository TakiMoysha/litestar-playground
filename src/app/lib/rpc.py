import threading
from queue import Queue, Empty
import time


class RPCConnection:
    """Unit of connection to RPC service."""

    def __init__(self, address):
        self.address = address
        self.connected = False

    def connect(self):
        time.sleep(0.1)  # Симуляция задержки подключения
        self.connected = True
        print(f"Connected to {self.address}")

    def disconnect(self):
        self.connected = False
        print(f"Disconnected from {self.address}")

    def call(self, data):
        if not self.connected:
            raise RuntimeError("Connection not established")
        return f"Response from {self.address}: {data}"


class RPCConnectionPool:
    def __init__(self, address, pool_size=5, max_overflow=10):
        self.address = address
        self.pool_size = pool_size
        self.max_overflow = max_overflow
        self.lock = threading.Lock()

        # Основные соединения
        self.pool = Queue(maxsize=pool_size)
        # "Переполненные" соединения (создаются при необходимости)
        self.overflow = 0

        # Наполнить пул заранее
        for _ in range(pool_size):
            conn = self._create_connection()
            self.pool.put(conn)

    def _create_connection(self):
        conn = RPCConnection(self.address)
        conn.connect()
        return conn

    def get_connection(self):
        with self.lock:
            try:
                # Попробовать взять соединение из пула
                return self.pool.get_nowait()
            except Empty:
                # Если пул пуст, создать "переполненное" соединение
                if self.overflow < self.max_overflow:
                    self.overflow += 1
                    return self._create_connection()
                else:
                    raise RuntimeError("Too many connections")

    def release_connection(self, conn):
        with self.lock:
            if self.pool.qsize() < self.pool_size:
                self.pool.put(conn)
            else:
                # Если пул заполнен, закрыть переполненное соединение
                self.overflow -= 1
                conn.disconnect()

    def close_all(self):
        while not self.pool.empty():
            conn = self.pool.get()
            conn.disconnect()


class RPCEngine:
    """Engine for executing RPC calls. Based on SQLAlchemy Engine."""

    def __init__(self, address, pool_size=5, max_overflow=10):
        self.pool = RPCConnectionPool(address, pool_size, max_overflow)

    def execute(self, data):
        """Выполняет RPC вызов через соединение из пула."""
        conn = self.pool.get_connection()
        try:
            response = conn.call(data)
            return response
        finally:
            self.pool.release_connection(conn)
