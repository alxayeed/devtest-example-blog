FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1 

RUN mkdir /example-project/

WORKDIR /example-project/ 

ADD . /example-project/ 

RUN pip install -r requirements.txt 

EXPOSE 8000 

CMD [ "python", "manage.py runserver 0.0.0.0:8000" ]
