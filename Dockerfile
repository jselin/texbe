FROM python:3.6.2-alpine

RUN apk add --no-cache gcc libc-dev libffi-dev openssl-dev make postgresql-dev openrc nginx


RUN mkdir /workdir

COPY requirements.txt /workdir/requirements.txt 
RUN pip install -r /workdir/requirements.txt

COPY . /workdir
WORKDIR /workdir

EXPOSE 8000

ENTRYPOINT ["./run.sh"]
