# Build an image that can do inference in SageMaker
# This is a Python 3 image that uses the nginx, gunicorn, flask stack
# for serving inferences in a stable way.

From ubuntu:18.04

MAINTAINER my-name@my-company.com

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         python \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN apt update
RUN apt install python3-pip -y

RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \
    pip3 install numpy==1.14.5 scipy scikit-learn pandas flask gevent gunicorn    
    

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

COPY code_base /opt/program
WORKDIR /opt/program
ENTRYPOINT ["python3", "train"]