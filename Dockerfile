FROM nvidia/cuda:11.0-devel-ubuntu20.04

COPY requirements.txt /root

RUN mkdir -p /root
COPY requirements.txt /root
WORKDIR /root

RUN apt-get update
RUN apt-get install git -y
RUN apt-get install vim -y

RUN apt-get install -y python3 python3-pip

RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

RUN pip3 install -r requirements.txt
