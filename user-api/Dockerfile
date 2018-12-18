FROM python:3.6.7

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

RUN mkdir -p /build
WORKDIR /build

COPY . /build

EXPOSE 8000

ENV C_FORCE_ROOT="true"
CMD ["honcho", "start"]