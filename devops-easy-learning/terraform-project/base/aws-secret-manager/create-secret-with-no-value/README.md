## How can I immediately delete a Secrets Manager secret so that I can create a new secret with the same name?

https://aws.amazon.com/premiumsupport/knowledge-center/delete-secrets-manager-secret/#:~:text=When%20you%20delete%20a%20secret,until%20the%20recovery%20window%20ends.

```
aws secretsmanager delete-secret --secret-id your-secret-name --force-delete-without-recovery --region your-region

aws secretsmanager delete-secret --secret-id  /2024/alertmanager --force-delete-without-recovery --region us-east-2
secretsmanager delete-secret --secret-id   /2024//sonarqube_db_password  --force-delete-without-recovery --region us-east-1
```