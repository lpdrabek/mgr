FROM python:3.6

COPY . /usr/src/app/
WORKDIR /usr/src/app/

RUN pip install setuptools -U

RUN python setup.py install
WORKDIR /usr/src/app/sweather
RUN pip freeze

