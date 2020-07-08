FROM python:3.7-slim

WORKDIR /app

ADD . /app

RUN apt-get install sudo

RUN sudo apt-get install libgomp1

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python"]

CMD ["/app/app.py"]
