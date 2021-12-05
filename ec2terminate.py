import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0f8a619a89716e8e8').terminate()