#
https://gitlab.com/gitlab-org/gitlab

## Gitlab file
Gitlab read a file call `.gitlab-cd.yml` by default when there is a change

## .gitlab-ci.yml keyword reference
https://docs.gitlab.com/ee/ci/yaml/


```yml
stages:    # List of stages for jobs, and their order of execution
  - build
  - push
  - test
  - deploy

build-job: # This job runs in the build stage, which runs first.
  stage: build
  script:
    - echo "Compiling the code..."
    - echo "Compile completed."
 
push-job:       # This job runs in the push stage.
  stage: build
  script:
    - echo "Pushing the code..."
    - echo "Push completed."

unit-test-job:   # This job runs in the test stage.
  stage: test    # It only starts when the job in the build stage completes successfully.
  script:
    - echo "Running unit tests... This will take about 60 seconds."
    - sleep 60
    - echo "Code coverage is 90%"

lint-test-job:   # This job also runs in the test stage.
  stage: test    # It can run at the same time as unit-test-job (in parallel).
  script:
    - echo "Linting code... This will take about 10 seconds."
    - sleep 10
    - echo "No lint issues found."

deploy-job:      # This job runs in the deploy stage.
  stage: deploy  # It only runs when *both* jobs in the test stage complete successfully.
  environment: production
  script:
    - echo "Deploying application in s3kemgou namespace..."
    - echo "Application successfully deployed"


##--------------------------------------------------------------------------------------------------


stages:     #The names and order of the pipeline stages.
   - clean
   - build
   - tag
   - login
   - push  

services:
  - docker:20.10.16-dind

clean-old-images:
  stage: clean 
  image: docker:20.10.16-dind    #Defines a job stage.
  script:            # to run commands
     - echo "Hello world"
     - ls
     - pwd


build-images:
  stage: build  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - echo "Hello world"
       
tag-images:
  stage: tag  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - echo "Hello world"
     - uname -r
     - mkdir test 
     - ls -l

dockerhub-login:
  stage: login  
  image: docker:latest    #Defines a job stage.
  script:            # to run commands
     - docker login -u devopseasylearning2021 -p DevOps2021@  docker.io
   
dockerhub-push:
  stage: push  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - echo "test"


##--------------------------------------------------------------------------------------------------

stages:     #The names and order of the pipeline stages.
   - clean
   - build
   - tag
   - login
   - push  

services:
  - docker:20.10.16-dind

clean-old-images:
  stage: clean 
  image: docker:20.10.16-dind    #Defines a job stage.
  script:            # to run commands
     - TAG=$(git log --pretty=format:'%h' -n 1)
     - docker rmi -f canary:$TAG || true 


build-images:
  stage: build  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - TAG=$(git log --pretty=format:'%h' -n 1)
     - docker build -t canary:$TAG .
     - docker images
       
tag-images:
  stage: tag  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - docker tag canary:$TAG devopseasylearning2021/s3:$TAG
     - docker images 


dockerhub-login:
  stage: login  
  image: docker:latest    #Defines a job stage.
  script:            # to run commands
     - docker login -u devopseasylearning2021 -p DevOps2021@   docker.io
     
       

dockerhub-push:
  stage: push  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - docker push devopseasylearning2021/s3:$TAG


##--------------------------------------------------------------------------------------------------
stages:     #The names and order of the pipeline stages.
   - clean
   - build
   - tag
   - login
   - push  

variables:
   APP: canary
   REPOSITORY: devopseasylearning2021
   PASSWORD: DevOps2021@
   REGISTRY: docker.io
services:
  - docker:20.10.16-dind

clean-old-images:
  stage: clean 
  image: docker:20.10.16-dind    #Defines a job stage.
  script:            # to run commands
     - docker rmi -f canary:$CI_COMMIT_SHORT_SHA || true 


build-images:
  stage: build  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - docker build -t canary:$CI_COMMIT_SHORT_SHA .
     - docker images
       
tag-images:
  stage: tag  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - docker tag canary:$CI_COMMIT_SHORT_SHA  devopseasylearning2021/s3:$CI_COMMIT_SHORT_SHA
     - docker images 


dockerhub-login:
  stage: login  
  image: docker:latest    #Defines a job stage.
  script:            # to run commands
     - docker login -u devopseasylearning2021 -p DevOps2021@   docker.io
     
       

dockerhub-push:
  stage: push  
  image: docker:20.10.16-dind      #Defines a job stage.
  script:            # to run commands
     - docker push devopseasylearning2021/s3:$CI_COMMIT_SHORT_SHA


##--------------------------------------------------------------------------------------------------

version: 0.2
### This buildspec is for the CI pipeline
phases:
  build:
    commands:
      - cd auth
      - docker build -t $IMAGE_REPO_NAME/weatherapp-auth:$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - cd ../UI
      - docker build -t $IMAGE_REPO_NAME/weatherapp-ui:$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - cd ../weather
      - docker build -t $IMAGE_REPO_NAME/weatherapp-weather:$CODEBUILD_RESOLVED_SOURCE_VERSION .


##--------------------------------------------------------------------------------------------------


version: 0.2
### This buildspec is for the delivery pipeline
phases:
  pre_build:
    commands:
      - curl -s https://get.helm.sh/helm-v3.7.2-linux-amd64.tar.gz  | tar xzf - linux-amd64/helm  --strip-components 1 && mv helm /usr/local/bin
      - curl -sL "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" -o /usr/local/bin/kubectl && chmod +x /usr/local/bin/kubectl
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $IMAGE_REPO_NAME
  build:
    commands:
      - cd auth
      - docker build -t $IMAGE_REPO_NAME/weatherapp-auth:$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - cd ../UI
      - docker build -t $IMAGE_REPO_NAME/weatherapp-ui:$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - cd ../weather
      - docker build -t $IMAGE_REPO_NAME/weatherapp-weather:$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - cd ..
  post_build:
    commands:
      - docker push $IMAGE_REPO_NAME/weatherapp-auth:$CODEBUILD_RESOLVED_SOURCE_VERSION
      - docker push $IMAGE_REPO_NAME/weatherapp-ui:$CODEBUILD_RESOLVED_SOURCE_VERSION
      - docker push $IMAGE_REPO_NAME/weatherapp-weather:$CODEBUILD_RESOLVED_SOURCE_VERSION
      - aws eks update-kubeconfig --name $EKS_CLUSTER_NAME 
      - cd weatherapp-auth
      - helm repo add bitnami https://charts.bitnami.com/bitnami
      - helm dependency build .
      - helm upgrade --install weatherapp-auth -n staging --set mysql.auth.rootPassword=$DB_PASSWORD --set image.repository=$IMAGE_REPO_NAME/weatherapp-auth --set image.tag=$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - cd ../weatherapp-ui
      - helm upgrade --install weatherapp-ui -n staging --set image.repository=$IMAGE_REPO_NAME/weatherapp-ui --set image.tag=$CODEBUILD_RESOLVED_SOURCE_VERSION .
      - cd ../weatherapp-weather
      - helm upgrade --install weatherapp-weather -n staging --set apikey=$API_KEY --set image.repository=$IMAGE_REPO_NAME/weatherapp-weather --set image.tag=$CODEBUILD_RESOLVED_SOURCE_VERSION .


##--------------------------------------------------------------------------------------------------
version: 0.2
### This buildspec is for the deployment pipeline
phases:
  pre_build:
    commands:
      - curl -s https://get.helm.sh/helm-v3.7.2-linux-amd64.tar.gz  | tar xzf - linux-amd64/helm  --strip-components 1 && mv helm /usr/local/bin
      - curl -sL "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" -o /usr/local/bin/kubectl && chmod +x /usr/local/bin/kubectl
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $IMAGE_REPO_NAME
  build:
    commands:
      - if ! $CI_COMMIT_TAG; then exit 1; fi
      - aws eks update-kubeconfig --name $EKS_CLUSTER_NAME 
      - cd weatherapp-auth
      - helm repo add bitnami https://charts.bitnami.com/bitnami
      - helm dependency build .
      - helm upgrade --install weatherapp-auth -n staging --set mysql.auth.rootPassword=$DB_PASSWORD --set image.repository=$IMAGE_REPO_NAME/weatherapp-auth --set image.tag=$CI_COMMIT_TAG .
      - cd ../weatherapp-ui
      - helm upgrade --install weatherapp-ui -n staging --set image.repository=$IMAGE_REPO_NAME/weatherapp-ui --set image.tag=$CI_COMMIT_TAG .
      - cd ../weatherapp-weather
      - helm upgrade --install weatherapp-weather -n staging --set apikey=$API_KEY --set image.repository=$IMAGE_REPO_NAME/weatherapp-weather --set image.tag=$CI_COMMIT_TAG .

##--------------------------------------------------------------------------------------------------
version: 0.2
### This buildspec is for the promotion pipeline
env:
  git-credential-helper: yes
phases:
  pre_build:
    commands:
      - cd /tmp
      - git clone $REPO_URL
      - cd $REPO_NAME
      - export TAGGED_HASH=`git rev-list -n 1 $CI_COMMIT_TAG`
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $IMAGE_REPO_NAME
  build:
    commands:
      - echo "Promoting Docker images"
      - docker pull $IMAGE_REPO_NAME/weatherapp-ui:$TAGGED_HASH
      - docker pull $IMAGE_REPO_NAME/weatherapp-auth:$TAGGED_HASH
      - docker pull $IMAGE_REPO_NAME/weatherapp-weather:$TAGGED_HASH
      - docker tag $IMAGE_REPO_NAME/weatherapp-ui:$TAGGED_HASH
      - docker tag $IMAGE_REPO_NAME/weatherapp-auth:$TAGGED_HASH
      - docker tag $IMAGE_REPO_NAME/weatherapp-weather:$TAGGED_HASH
  post_build:
    commands:
      - docker push $IMAGE_REPO_NAME/weatherapp-auth:$CI_COMMIT_TAG
      - docker push $IMAGE_REPO_NAME/weatherapp-ui:$CI_COMMIT_TAG
      - docker push $IMAGE_REPO_NAME/weatherapp-weather:$CI_COMMIT_TAG
```