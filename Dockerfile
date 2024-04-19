FROM python:3.8-slim as base

RUN apt-get update && \
    apt-get install -y libcurl4-openssl-dev && \
    find /var/*/apt -type f -delete

RUN pip install --no-cache-dir Flask-SQLAlchemy \
    SQLAlchemy \
    beautifulsoup4 \
    nltk \
    markdown \
    Flask-Assets \
    google-api-python-client \
    gunicorn 

FROM base AS final

WORKDIR /app

COPY . /app

RUN python3 content_to_db.py

# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0

# EXPOSE 5000


# CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]