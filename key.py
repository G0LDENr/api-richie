import boto3

def get_secret_value(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']

def set_secret_value(secret_name, secret_value):
    client = boto3.client('secretsmanager')
    response = client.put_secret_value(
        SecretId=secret_name,
        SecretString=secret_value
    )
    return response