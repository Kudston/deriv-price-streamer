FROM python:3.12-bookworm

WORKDIR /src
COPY requirements.txt .

RUN python -m venv /opt/venv
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/opt/venv/bin/python", "-m", "src.main"]
