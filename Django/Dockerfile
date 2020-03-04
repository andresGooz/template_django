FROM python:3.8.1
RUN mkdir /Django
WORKDIR /Django
COPY requirements.txt /Django/
RUN pip install -r requirements.txt
COPY . /Django/
