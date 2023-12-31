FROM python:3.7-slim-buster

WORKDIR /api.py

COPY . /api.py

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3300

ENV NAME World

CMD ["python","api.py"]


