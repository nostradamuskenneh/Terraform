
## Gitlab Pipeline

### This stage can run on every branches except develop and master
```yaml
push-commit:
   stage: push-commit
   script:
    - echo "good"
   except:
    - develop
    - master
   tags:
     - n3shell
```

### This stage can only run on develop and master
```yaml
build-develop:
   stage: build-develop
   script:
     - echo "good"
   only:
     - develop
     - master
```

### This is the order of execution
```yaml
stages:
   - clean
   - build
   - test
   - coverage-test
   - sonarqube
   - build-commit
   - push-commit
   - build-develop
   - push-develop
   - push-production
   - deploy-dev
   - deploy-production
```

### All stages will used n1shell by default if we don't specify a runner at each stage. Each stage will retry 1 time
```yaml
default:
   tags:
     - n1shell
   retry: 1
```

### This stage will retry 2 times if the built failed
```yaml
build-commit:
   stage: build-commit
   script:
    - echo "good"
   except:
    -  develop
    - master
   retry: 2
```

### Define variables
- define it at the group level
- onder settings - go to CICD - variable
```yaml
stages:
   - clean
   - build

default:
   tags:
     - n1shell
   retry: 1

variables: 
   DB_PASSWORD: test
   DB_USERNAME: admin

login_build_push:
   stage: build
   script:
      - docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD
      - docker push $DOCKERHUB_USERNAME/$APP:$CI_COMMIT_BRANCH
   after_script: docker rmi $DOCKERHUB_USERNAME/$APP:$CI_COMMIT_BRANCH 
   allow_failure: false
```

### If you want the stage to run the same time, git the stage the same name

```yaml
# This will runs one after another
stages:
   - clean
   - build
   - test
  
default:
   tags:
     - n1shell
   retry: 1

clean:
   stage: clean
   script:
    - echo "good"
   before_script:
    - echo "looks good"
   allow_failure: true

build:
   stage: build
   script:
    - echo "good"

test:
   stage: test
   script:
    - echo "good"
   allow_failure: true


# This will runs in parallel or at the same time
stages:
   - clean
   - build
   - test
  
default:
   tags:
     - n1shell
   retry: 1

clean:
   stage: Pipeline_stage
   script:
    - echo "good"
   before_script:
    - echo "looks good"
   allow_failure: true

build:
   stage: Pipeline_stage
   script:
    - echo "good"

test:
   stage: Pipeline_stage
   script:
    - echo "good"
   allow_failure: true
```


### needs: it is used to handle depend-on
- this means build and test depend-on clean
- this means clean will runs first
```yaml
# This will runs one after another
stages:
   - clean
   - build
   - test
  
default:
   tags:
     - n1shell
   retry: 1

clean:
   stage: clean
   script:
    - echo "good"
   before_script:
    - echo "looks good"
   allow_failure: true
   needs: [] # this is a reference

build:
   stage: build
   script:
    - echo "good"
   needs: ["clean"]

test:
   stage: test
   script:
    - echo "good"
   allow_failure: true
   needs: ["clean"]
```

### If you don't the stage to run, put `.` infront of the stage
- in this example, the clean and build stage will not run
```yaml
stages:
   - clean
   - build
   - test
  
default:
   tags:
     - n1shell
   retry: 1

.clean:
   stage: Pipeline_stage
   script:
    - echo "good"
   before_script:
    - echo "looks good"
   allow_failure: true

.build:
   stage: Pipeline_stage
   script:
    - echo "good"

test:
   stage: Pipeline_stage
   script:
    - echo "good"
   allow_failure: true
```











```yaml
stages:
   - clean
   - build
   - test
   - coverage-test
   - sonarqube
   - build-commit
   - push-commit
   - build-develop
   - push-develop
   - push-production
   - deploy-dev
   - deploy-production

default:
   tags:
     - n1shell
   #   - n4shell
   #   - n3shell
   retry: 1

variables: 
   APP: test
   PROJECT: practise

clean:
   stage: clean
   script:
    - echo "good"
   before_script:
   - echo "looks good"
   allow_failure: true

build:
   stage: build
   script:
    - echo "good"


test:
   stage: test
   script:
    - echo "good"
   allow_failure: true

coverage-test:
   stage: coverage-test
   script:
    - echo "good"


sonarqube:
   stage: sonarqube
   script:
    - echo "good"


build-commit:
   stage: build-commit
   script:
    - echo "good"
   except:
    -  develop
    - master
   tags:
     - n3shell

push-commit:
   stage: push-commit
   script:
    - echo "good"
   except:
    -  develop
    - master
   tags:
     - n3shell
  

build-develop:
   stage: build-develop
   script:
     - echo "good"
   only:
     - develop
     - master
   retry: 2
   variables: 
      APP1: test1
      PROJECT1: practise1
      APP12: test12
      PROJECT12: practise12


push-develop:
   stage: push-develop
   script:
    - echo "good"
   only:
     - develop
     - master
   retry: 2
   variables: 
      APP1: test1
      PROJECT1: practise1
      APP12: test12
      PROJECT12: practise12

push-production: 
   stage: push-production
   script:
    - echo "good"
   only:
    - master
   variables: 
      APP12: test12
      PROJECT12: practise12


deploy-dev:
   stage: deploy-dev
   script:
    - echo "good"
   only:
     - develop
   tags:
     - n4shell
   retry: 2
   variables: 
      APP1: test1
      PROJECT1: practise1


deploy-production:
   stage: deploy-production
   script:
    - echo "good"
   only:
     - master
   tags:
     - n1shell
   retry: 2
   variables: 
      APP12: test12
      PROJECT12: practise12
```