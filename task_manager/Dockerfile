FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /usr/src/anna/
WORKDIR /usr/src/

ADD requirements.txt /usr/src/anna/
RUN pip install -r anna/requirements.txt
ADD . /usr/src/anna/

CMD python manage.py runserver -h 0.0.0.0