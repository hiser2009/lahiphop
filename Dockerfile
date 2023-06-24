FROM python:alpine3.16
# FROM python:latest

WORKDIR /events

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD ["event.py"]