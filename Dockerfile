FROM python:3.8

COPY ./requirements.txt /app/requirements.txt

COPY main.py /app/main.py

RUN pip install -r /app/requirements.txt

EXPOSE 8000

COPY / /app

WORKDIR /app

CMD ["python3", "uvicorn ", "app.main:app", "--host 0.0.0.0"]