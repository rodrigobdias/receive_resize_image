FROM ubuntu

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN mkdir -p /home/receive_image
WORKDIR /home/receive_image

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libsm6 libxext6 libxrender-dev

ENV FLASK_APP receive_image.py
ENV FLASK_DEBUG 0
ENV FLASK_RUN_HOST 0.0.0.0

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY receive_image.py receive_image.py
COPY conf_receive_rabbitmq.py conf_receive_rabbitmq.py
COPY start_receive_image.sh start_receive_image.sh
COPY __init__.py __init__.py

CMD ["flask", "run"]