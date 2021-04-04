FROM tiangolo/uvicorn-gunicorn:python3.8

COPY ./app/requirements.txt .

RUN pip install -r requirements.txt 

WORKDIR /app
