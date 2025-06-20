import pytest

from app.lib.rpc import RPCEngine


def test_rpc_engine_creation():
    engine = RPCEngine("rpc://example-service", pool_size=2, max_overflow=3)

    # Симуляция параллельных запросов
    def worker(task_id):
        print(f"Worker {task_id} started")
        response = engine.execute(f"Task {task_id}")
        print(f"Worker {task_id} got response: {response}")

    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            executor.submit(worker, i)

    # Закрытие всех соединений
    engine.pool.close_all()
