FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000 5443

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Create startup script
RUN echo '#!/bin/bash\n\
if [ -f "/etc/letsencrypt/live/$DOMAIN/fullchain.pem" ]; then\n\
  echo "Starting with HTTPS support"\n\
  gunicorn --bind 0.0.0.0:5000 --workers 4 app:app &\n\
  gunicorn --bind 0.0.0.0:5443 --workers 4 --certfile=/etc/letsencrypt/live/$DOMAIN/fullchain.pem --keyfile=/etc/letsencrypt/live/$DOMAIN/privkey.pem app:app\n\
else\n\
  echo "Starting with HTTP only"\n\
  gunicorn --bind 0.0.0.0:5000 --workers 4 app:app\n\
fi' > /app/start.sh && chmod +x /app/start.sh

CMD ["/app/start.sh"]