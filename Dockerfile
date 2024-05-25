FROM python:3.12.2-bookworm

WORKDIR /app

COPY ./server /app

RUN pip install -r /app/requirements.txt

CMD ["python", "main.py"]