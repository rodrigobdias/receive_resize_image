FROM ubuntu

WORKDIR /home/resizing_image

ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y libsm6 libxext6 libxrender-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY resizing_image.py ./
COPY conf_resizing_rabbitmq.py ./
COPY start_resizing_image.sh ./
COPY __init__.py ./

# runtime configuration
EXPOSE 5000

#ENTRYPOINT ["./boot.sh"]
#ENTRYPOINT ["top", "-b"]
#CMD ["-c"]
