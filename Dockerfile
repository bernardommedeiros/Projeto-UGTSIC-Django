# Imagem python baseada no debian bullseye (slim)
FROM python:3.11.3-slim-bullseye
LABEL mantainer="bernardo181105@gmail.com"

# Impede o Python de gravar arquivos de bytecode (.pyc) no disco. 1 = Não, 0 = Sim
ENV PYTHONDONTWRITEBYTECODE 1

# Saída do Python será exibida imediatamente no console ou em  outros dispositivos de saída, sem ser armazenada em buffer. Em resumo, visualizar os outputs do Python em tempo real.
ENV PYTHONUNBUFFERED 1

COPY /src/ugtsic_project /ugtsic_project

COPY scripts /scripts

# Diretório de trabalho dentro do container
WORKDIR /src/ugtsic_project

EXPOSE 3333

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /ugtsic_project/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod +x /scripts/commands.sh && \
  apt-get update && \
  apt-get install -y bash postgresql-client

ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["bash", "commands.sh"]