## GitHub Actions
- Docker containers with GitHub Actions [here](https://www.youtube.com/watch?v=09lZdSpeHAk)
- GitHub link [here](https://github.com/marcel-dempers/docker-development-youtube-series/tree/master/.github/workflows)


```yml
name: Docker Series Builds

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    # runs-on: [self-hosted, linux]
    steps:
    - uses: actions/checkout@v2
    - name: docker login
      env:
        DOCKER_USER: ${{ secrets.DOCKER_USER }}   
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}  
      run: |
        docker login -u $DOCKER_USER -p $DOCKER_PASSWORD
    - name: docker build csharp
      run: |
        docker build ./c# -t aimvector/csharp:1.0.0
    - name: docker build nodejs
      run: |
        docker build ./nodejs -t aimvector/nodejs:1.0.0
    - name: docker build python
      run: |
        docker build ./python -t aimvector/python:1.0.0
    - name: docker build golang
      run: |
        docker build ./golang -t aimvector/golang:1.0.0
    - name: docker push
      run: |
        docker push aimvector/csharp:1.0.0
        docker push aimvector/nodejs:1.0.0
        docker push aimvector/golang:1.0.0
        docker push aimvector/python:1.0.0


name: GitHub Actions Demo
run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v3
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```


https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions

https://github.com/cypress-io/github-action/blob/master/.github/workflows/example-basic.yml

https://github.com/marketplace/actions/yaml-update-action

https://github.com/aws-actions/amazon-ecr-login

https://github.com/marketplace/actions/docker-login


### AWS Public Elastic Container Registry (ECR)
```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Public ECR
        uses: docker/login-action@v2
        with:
          registry: public.ecr.aws
          username: ${{ secrets.AWS_ACCESS_KEY_ID }}
          password: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        env:
          AWS_REGION: <region>
```

### GitLab
```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to GitLab
        uses: docker/login-action@v2
        with:
          registry: registry.gitlab.com
          username: ${{ secrets.GITLAB_USERNAME }}
          password: ${{ secrets.GITLAB_PASSWORD }}
```

### GitHub Container Registry
```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to GitHub Container Registry
        uses: docker/login-action@v2
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
```

### Docker Hub
```yaml
name: ci

on:
  push:
    branches: main

jobs:
  login:
    runs-on: ubuntu-latest
    steps:
      -
        name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
```