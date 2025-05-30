

## Generate Certificate and Run with it
```bash
# Generate tmp/server.crt and tmp/server.key (as x509)
uv run tooling/certificate.py

# Run server with self-signed certificate
uv run app run --create-self-signed-cert \
  --ssl-certfile=tmp/server.crt \
  --ssl-keyfile=tmp/server.key
```
