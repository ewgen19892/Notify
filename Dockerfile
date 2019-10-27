FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y netcat
RUN mkdir -p /app && mkdir -p /app/storage/static && mkdir -p /app/storage/media && mkdir -p /app/logs
WORKDIR /app
ADD requirements.txt /app
RUN pip install --upgrade pip && pip3 install -r requirements.txt
ADD . /app


ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["prod"]
