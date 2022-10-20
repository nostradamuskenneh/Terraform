## How can I immediately delete a Secrets Manager secret so that I can create a new secret with the same name?

https://aws.amazon.com/premiumsupport/knowledge-center/delete-secrets-manager-secret/#:~:text=When%20you%20delete%20a%20secret,until%20the%20recovery%20window%20ends.

```
aws secretsmanager delete-secret --secret-id your-secret-name --force-delete-without-recovery --region your-region

aws secretsmanager delete-secret --secret-id  /2024/alertmanager --force-delete-without-recovery --region us-east-2
secretsmanager delete-secret --secret-id   /2024//sonarqube_db_password  --force-delete-without-recovery --region us-east-1
```

```
aws secretsmanager delete-secret --secret-id databases-username --force-delete-without-recovery --region us-east-1
aws secretsmanager delete-secret --secret-id database-password --force-delete-without-recovery --region us-east-1
aws secretsmanager delete-secret --secret-id 2568/adl/db/databases-username --force-delete-without-recovery --region us-east-1
aws secretsmanager delete-secret --secret-id 2568/adl/db/databases-password --force-delete-without-recovery --region us-east-1
aws secretsmanager delete-secret --secret-id prod-mam-rds-username --force-delete-without-recovery --region us-east-1
aws secretsmanager delete-secret --secret-id prod-mam-rds-password --force-delete-without-recovery --region us-east-1
```

/*
RESULT:
Outputs:
rds_password = <sensitive>
rds_username = <sensitive>
*/

/*
// CREATE A DATABASE WITH USERNAME AND PASSWORD
password = data.aws_secretsmanager_secret_version.rds-password.secret_string
username = data.aws_secretsmanager_secret_version.rds-username.secret_string
*/






