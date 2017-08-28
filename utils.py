import boto3
from botocore.exceptions import ClientError
from configs import configs


def get_users(event=None, context=None):
    table = boto3.resource('dynamodb').Table(configs['table'])
    users = []
    args = {}
    try:
        response = table.scan(**args)
        users = response['Items']
        while 'LastEvaluatedKey' in response:
            args["ExclusiveStartKey"] = response['LastEvaluatedKey']
            response = table.scan(**args)
            users += response['Items']
    except ClientError as err:
        return {}
    return users
