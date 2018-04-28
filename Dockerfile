FROM python:2.7.10-wheezy
MAINTAINER Zheng Guang "zg.zhu@daocloud.io"

WORKDIR /code

RUN echo "Asia/Shanghai" > /etc/timezone && \
        dpkg-reconfigure -f noninteractive tzdata
RUN apt-get update && apt-get -qqy install python-pip && pip install --upgrade pip

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD . /code
RUN mkdir -p  static &&  ln -s ../qr.png static/qr.png

EXPOSE 8000


# Start python
CMD ["python2", "app.py"]
