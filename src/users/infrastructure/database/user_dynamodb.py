import boto3, sys
from users.domain.user_database import UserDatabase
from werkzeug.security import generate_password_hash
from users.domain.user_exception import UserException
from botocore.exceptions import ClientError

class UserDynamoDB(UserDatabase):
    def __init__(self):
        self.client = boto3.resource('dynamodb', region_name="eu-west-3", endpoint_url='http://dynamodb:8000', aws_access_key_id="root", aws_secret_access_key="root")

    def users_table(self):
        try:
            table = self.client.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'username',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'username',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
            )
            table.meta.client.get_waiter('table_exists').wait(TableName='users')

            table.put_item(
            Item={ 
                    'username': "John",
                    'password': generate_password_hash("aaa",method='sha256'),
                    'role': "admin"
            })
            table.put_item(
                Item={
                        'username': "Pepito",
                        'password': generate_password_hash("eee",method='sha256'),
                        'role': "user"
                })
            table.put_item(
                Item={
                        'username': "test",
                        'password': generate_password_hash("test",method='sha256'),
                        'role': "test"
                })

        except Exception:
            table = self.client.Table('users')
        return table
    
    def create(self, user):
        try:
            self.users_table().put_item(
                Item={
                    'username': user.username,
                    'password': user.password,
                    'role': user.role
                },
                ConditionExpression='attribute_not_exists(username)'
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                raise UserException("There is a conflict to create this resource",409)
        return "Added"

    def find(self, username):
        response = self.users_table().get_item(
            Key={
                "username": username
            }
        )
        return response['Item']
    
    def update(self,username,password,role):
        self.users_table().update_item(
            Key={
                'username': username
            },
            UpdateExpressions='SET password = :val1, role = :val2',
            ExpressionAttributeValues={
                ':val1': generate_password_hash(password,method='sha256'),
                ':val2': role
            }
        )
        return "Updated"