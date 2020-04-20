FROM ubuntu

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN mkdir -p /home/resizing_image
WORKDIR /home/resizing_image

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libsm6 libxext6 libxrender-dev

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY conf_resizing_rabbitmq.py conf_resizing_rabbitmq.py
COPY __init__.py __init__.py
COPY resizing_image.py resizing_image.py

CMD [ "python3", "./resizing_image.py" ]
