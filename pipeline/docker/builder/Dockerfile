FROM ubuntu:latest
RUN apt-get update -y
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ 'Europe/Tallinn'
RUN apt-get update && apt-get install -y tzdata && \
    apt-get install apt-utils -y \
    wget \
    curl \
    vim \
    unzip \
    tree \
    git \
    default-jre \
    default-jdk \
    python3-pip \
    ansible \
    make 

### AWS CLI INSTALLATIN
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && aws/install \
    # && aws/install -i /usr/local/aws-cli -b /usr/local/bin \
    && rm -rf awscliv2.zip \
    && rm -rf aws

### AZURE CLI INSTALLATIN
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

### KUBECTL INSTALLATIN
RUN curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.17.9/2020-08-04/bin/linux/amd64/kubectl \
    && chmod +x ./kubectl \
    && mv kubectl /usr/local/bin/

### INSTALL KUBECTX AND KUBENS
RUN wget https://raw.githubusercontent.com/ahmetb/kubectx/master/kubectx \
    && wget https://raw.githubusercontent.com/ahmetb/kubectx/master/kubens \
    && chmod +x kubectx kubens \
    && mv kubens kubectx /usr/local/bin

### TERRAFORM INSTALLATIN
ENV TERRAFORM_VERSION 1.0.0
WORKDIR /tmp
RUN wget -q https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
    && mv terraform /usr/local/bin \
    && rm -f terraform terraform_${TERRAFORM_VERSION}_linux_amd64.zip

### TERRAGRUNT INSTALLATIN
ENV TERRAGRUNT_VERSION v0.26.7
RUN wget https://github.com/gruntwork-io/terragrunt/releases/download/${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 \
    && mv terragrunt_linux_amd64 terragrunt \
    && chmod u+x terragrunt \
    && mv terragrunt /usr/local/bin/terragrunt

### HELM INSTALLATIN
RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 \
    && chmod +x get_helm.sh && ./get_helm.sh


