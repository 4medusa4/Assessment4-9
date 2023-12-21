FROM python:3.7-slim-buster

WORKDIR /api.py

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 3300

ENV NAME World

CMD ["python","api.py"]


