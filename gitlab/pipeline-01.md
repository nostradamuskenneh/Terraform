
```yml
stages:
  - tag
  - build-UI
  - build-db
  - build-auth
  - build-weather
  - login-push
default:
  tags:
    - n1shell
tag:
   stage: tag
   script:
     - TAG=`git rev-parse --short=4  HEAD`
     - echo "TAG=$TAG" >> build.env
   artifacts:
     reports:
       dotenv: build.env

build-UI:
  stage: build-UI
  script:
    - cd UI
    - docker build -t $DOCKERHUB_USERNAME/s4-ui:$TAG .
    - cd -

build-db:
  stage: build-db
  script:
    - cd DB
    - docker build -t $DOCKERHUB_USERNAME/s4-db:$TAG .
    - cd -

build-auth:
  stage: build-auth
  script:
    - cd auth
    - docker build -t $DOCKERHUB_USERNAME/s4-auth:$TAG .
    - cd -

build-weather:
  stage: build-weather
  script:
    - cd weather
    - docker build -t $DOCKERHUB_USERNAME/s4-weather:$TAG .
    - cd -

login-push:
  stage: login-push
  script:
    - docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD
    - docker push $DOCKERHUB_USERNAME/s4-ui:$TAG
    - docker push $DOCKERHUB_USERNAME/s4-db:$TAG
    - docker push $DOCKERHUB_USERNAME/s4-auth:$TAG
    - docker push $DOCKERHUB_USERNAME/s4-weather:$TAG
