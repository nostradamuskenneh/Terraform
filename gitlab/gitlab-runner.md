
##
- install a runner
- register the runner (switch to `gitlab-runner` user) [here](https://www.fosstechnix.com/how-to-install-gitlab-runner-on-ubuntu/
)
- We can cofigure runner at
    - The group level : This a share running (all subgroup and project can use it)
    - The subgroup level : This a share running (all projects under this subgroup can use it)
    - The project level : runner (only project can use it)
        - shell runners means we want to run shell commands
        - docker runners means we want to run docker commands
- Runner are configured at the group level

https://docs.gitlab.com/runner/configuration/advanced-configuration.html

https://gitlab.com/gitlab-org/gitlab-runner/-/blob/main/config.toml.example


```sh
sudo gitlab-runner register \
  --non-interactive \
  --url "GITLAB_SERVER_URL" \
  --registration-token "REGISTRATION_TOKEN" \
  --description "docker-runner" \
  --executor "docker" \
  --docker-image ubuntu:latest
```