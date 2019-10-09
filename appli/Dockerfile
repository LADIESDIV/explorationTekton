FROM python:3.7.2-alpine3.9

RUN pip install Flask

WORKDIR /app.py
COPY . /app.py

EXPOSE 5000

ENV FLASK_APP app.py

CMD ["python", "app.py", "-h", "0.0.0.0"]