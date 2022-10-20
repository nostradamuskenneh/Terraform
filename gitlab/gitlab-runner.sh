
## Install docker
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
 sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin -y 
chmod 666 /var/run/docker.sock

## Install Gitlab runner
# https://www.fosstechnix.com/how-to-install-gitlab-runner-on-ubuntu/
apt update -y
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash
sudo apt-get install gitlab-runner
apt-cache madison gitlab-runner
sudo apt-get install gitlab-runner=15.0.0
sudo gitlab-runner -version
sudo gitlab-runner status
sudo gitlab-runner start
sudo gitlab-runner stop
sudo gitlab-runner restart
echo -e 'gitlab-runner  ALL=(ALL)  NOPASSWD:  ALL' > /etc/sudoers.d/gitlab-runner
echo -e 'gitlab-runner  ALL=(ALL:ALL) ALL' > /etc/sudoers.d/gitlab-runner
usermod gitlab-runner -aG docker 


## Register Runners and update the config.toml in /etc/gitlab-runner/
t="$TOKEN"
gitlab-runner -l debug register \
--non-interactive \
--url ${GITLAB_URL} \
--registration-token ${t} \
  --executor docker \
  --docker-image python3 \
  --name TestRunner \
  --docker-pull-policy always \ # always, if-not-present, never: only uses the local version (never download an image).
  --locked=false \ # if true, tag can only be used for a specify project, if false, it can be used for all projects
  --run-untagged=false \
  --docker-privileged=false \
  --limit 0 \
  --tag-list general,test

gitlab-runner -l debug register \
    --non-interactive \
    --url "https://gitlab.com" \
    --registration-token "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" \
    --executor shell \
    --docker-image ubuntu \
    --name shell-01 \
    --docker-pull-policy always \
    --locked=false \
    --run-untagged=false \
    --docker-privileged=false \
    --limit 0 \
    --tag-list shell-01

gitlab-runner -l debug register \
    --non-interactive \
    --url "https://gitlab.com" \
    --registration-token "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" \
    --executor shell \
    --docker-image ubuntu \
    --name shell-02 \
    --docker-pull-policy always \
    --locked=false \
    --run-untagged=false \
    --docker-privileged=false \
    --limit 0 \
    --tag-list shell-02


gitlab-runner -l debug register \
    --non-interactive \
    --url "https://gitlab.com" \
    --registration-token "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" \
    --executor docker \
    --docker-image ruby:2.7 \
    --name docker-01 \
    --docker-pull-policy always \
    --locked=false \
    --run-untagged=false \
    --docker-privileged=false \
    --limit 0 \
    --tag-list docker-01

gitlab-runner list
gitlab-runner Register
gitlab-runner verify
