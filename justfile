set dotenv-load


dev *ARGS:
  uv run app

litestar-create-certificate:
  uv run litestar run --ssl-certfile=server.crt --ssl-keyfile=server.key --create-self-signed-cert
