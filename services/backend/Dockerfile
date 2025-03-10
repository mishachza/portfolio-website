FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 5000

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]