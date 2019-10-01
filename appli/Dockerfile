FROM python:3.7.2-alpine3.9

RUN pip install Flask

WORKDIR /server.py

COPY . /server.py

EXPOSE 5000

ENV FLASK_APP server.py

CMD ["python", "-m", "flask", "run", "-h", "0.0.0.0"]