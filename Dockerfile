FROM python:3.9

RUN apt-get update

WORKDIR /code

RUN pip install --upgrade pip

EXPOSE 14552/udp

COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

COPY . /code

CMD ["python", "./src/main.py"]
