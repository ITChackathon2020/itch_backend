FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


ENTRYPOINT ["sh", "run_deploy.sh"]