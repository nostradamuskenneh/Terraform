echo 'tar $JENKINS_HOME directory'
set +e 
tar -cvf jenkins_backup.tar -C $JENKINS_HOME .
exitcode=$?
if [ "$exitcode" != "1" ] && [ "$exitcode" != "0" ]; then
exit $exitcode
fi
set -e
echo 'Upload jenkins_backup.tar to S3 bucket'
aws s3 cp jenkins_backup.tar s3://ekteck-jenkins-backup/
echo 'Remove files after succesful upload to S3'
rm -rf *