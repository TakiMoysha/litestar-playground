## Generate Certificate and Run with it

```bash
# Generate tmp/server.crt and tmp/server.key (as x509)
uv run tooling/certificate.py

# Run server with self-signed certificate
uv run app run --create-self-signed-cert \
  --ssl-certfile=tmp/server.crt \
  --ssl-keyfile=tmp/server.key
```

## Engine for RPC persistence connection

_ConnectionPool_ - для управления соединениями. Эти соединения переиспользуются между запросами.

_Issues with Gateway Serves_ - gateway server работает как несколько процессов (daphna, uvicorn...). ConnectionPool будет создаваться для каждого процесса свой.

_LazyConnection_ - установка соединений только при необходимости.
