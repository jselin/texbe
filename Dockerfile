FROM python:3.6.2-alpine

RUN apk add --no-cache gcc libc-dev libffi-dev openssl-dev make postgresql-dev openrc nginx


RUN mkdir /workdir

COPY requirements.txt /workdir/requirements.txt 
RUN pip install -r /workdir/requirements.txt

COPY . /workdir
WORKDIR /workdir

EXPOSE 8000

ENV RDS_DB_NAME='texdesigners'
ENV RDS_USERNAME='jkselin'
ENV RDS_PASSWORD=''
ENV RDS_HOSTNAME='localhost'
ENV RDS_PORT=''
ENV SECRET_KEY='df8856afe0832f4fb42095daa92ca9a0ddbed40f'
ENV DJANGO_DEVELOPMENT=true

#COPY ./run.sh /
ENTRYPOINT ["./run.sh"]
