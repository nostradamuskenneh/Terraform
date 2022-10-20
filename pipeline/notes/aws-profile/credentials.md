## PROFILE 

[How to set up and work with AWS CLI profiles](https://www.youtube.com/watch?v=ptbxhz7TWmE)

### Run commands with profile
```
aws s3 ls --profile tia
aws s3 ls --profile dev
aws s3 ls --profile prod
```

### credentials
```
[default]
aws_access_key_id = AKIAUZUQ3FGTRF3KJ6G4TVYCY
aws_secret_access_key = XJFwXUss8dddODgfdDSolLX+CjQXvHddetds9h6fH1isORT5emj

[dev]
aws_access_key_id = AKIAUZUQ3FGTRF3KJ6G4TVYCY
aws_secret_access_key = XJFwXUss8dddODgfdDSolLX+CjQXvHddetds9h6fH1isORT5emj

[qa]
aws_access_key_id = AKIA5MTCFRFFYFMJL62XBG6N4
aws_secret_access_key = IWPKAmdC3YSggfdXv2tP1unQSOykqGb6WP7V28Tz+2C98 

[prod]
aws_access_key_id = AKIRRA3PBICGTRERDDCHJCBUC4W
aws_secret_access_key = QNiW8KnIHLfgghYyJBkiLL9jFSQ8G7m+LN0PrhJ8TnIl
```

### Switch between profile
we need to export the profile every time that we need to switch to 
```
export AWS_PROFILE=dev
export AWS_PROFILE=qa
export AWS_PROFILE=prod
```

### list all the export profile
```
echo $AWS_PROFILE
```

### Check from AWS
```
aws sts get-caller-identity

alias awsd='export AWS_PROFILE=dev'
alias awsp='export AWS_PROFILE=prod'
alias awst='export AWS_PROFILE=tia'
alias awsp='echo $AWS_PROFILE'
alias awsg='aws sts get-caller-identity'
alias s3='aws s3 ls'
```