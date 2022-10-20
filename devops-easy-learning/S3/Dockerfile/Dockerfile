# FROM
# RUN
# ARG
# COPY
# ADD
# USER
# ENV
# WORKDIR
# LABEL
# EXPOSE
# MAINTAINER


# CMD
# ENTRYPOINT


# VOLUME




FROM ubuntu
RUN mkdir -p /tmp/tia-test
RUN touch /test.txt

ENV TZ=America/Phoenix
ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y
RUN apt-get install -y tzdata 
RUN apt-get install -y apt-utils 
RUN apt install -y wget
RUN apt install -y curl
RUN apt install -y tree
RUN apt install -y git
RUN apt install -y make
RUN apt install -y unzip
RUN apt install -y ansible
RUN apt install -y python3-pip

RUN apt update -y && \
    apt-get install -y tzdata && \
    apt-get install -y apt-utils && \
    apt install -y wget && \
    apt install -y curl && \
    apt install -y tree && \
    apt install -y git && \
    apt install -y make && \
    apt install -y unzip && \
    apt install -y ansible && \
    apt install -y vim && \
    apt install -y python3-pip 

### TERRAFORM INSTALLATION
## https://releases.hashicorp.com/terraform/

RUN wget https://releases.hashicorp.com/terraform/1.0.0/terraform_1.0.0_linux_amd64.zip
RUN unzip terraform_1.0.0_linux_amd64.zip 
RUN mv terraform /usr/local/bin
RUN rm -rf terraform_1.0.0_linux_amd64.zip


FROM ubuntu
RUN apt update -y && \
    apt install -y wget && \
    apt install -y curl && \
    apt install -y unzip && \
    apt install -y vim  

### TERRAFORM INSTALLATIN
ENV TERRAFORM_VERSION1 1.0.0
ENV TERRAFORM_VERSION012 0.12.31
RUN mkdir /tia-temp
WORKDIR /tia-temp

RUN wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION1}/terraform_${TERRAFORM_VERSION1}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION1}_linux_amd64.zip \
    && mv terraform /usr/local/bin/ \
    && rm -f terraform terraform_${TERRAFORM_VERSION1}_linux_amd64.zip 

RUN wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION1}/terraform_${TERRAFORM_VERSION1}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION1}_linux_amd64.zip \
    && mv terraform /usr/local/bin/tf1 \
    && rm -f terraform terraform_${TERRAFORM_VERSION1}_linux_amd64.zip 

RUN wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION012}/terraform_${TERRAFORM_VERSION012}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION012}_linux_amd64.zip \
    && mv terraform /usr/local/bin/tf12 \
    && rm -f terraform terraform_${TERRAFORM_VERSION012}_linux_amd64.zip 


## KUBECTL INSTALLATION
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
RUN kubectl version



FROM httpd
ARG port=80
ARG user=root
ARG web=covid19

LABEL maintainer="Tia M"
RUN apt -y update && \
    apt -y install wget && \
    apt -y install unzip

WORKDIR /usr/local/apache2/htdocs/

RUN rm -rf * && \
    wget https://linux-devops-course.s3.amazonaws.com/WEB+SIDE+HTML/${web}.zip && \
    unzip ${web}.zip && \
    cp -R ${web}/* . && \
    rm -rf ${web}.zip && \
    rm -rf ${web}

USER ${user}
ENTRYPOINT ["httpd-foreground"]
EXPOSE ${port}


FROM centos:centos7
LABEL Create by tia
ENV NAME tia 
RUN mkdir /test-copy
RUN mkdir /test-add-local
RUN mkdir /test-add-remote

COPY ./covid19.zip /test-copy
ADD ./covid19.zip /test-add-local
ADD https://linux-devops-course.s3.amazonaws.com/WEB+SIDE+HTML/covid19.zip /test-add-remote

WORKDIR /test-copy
RUN useradd $NAME
