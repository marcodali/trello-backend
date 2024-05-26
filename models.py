import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')
table = dynamodb.Table('Cards')

class Card:
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    @staticmethod
    def get_card(id):
        response = table.get_item(Key={'id': id})
        return response.get('Item')

    @staticmethod
    def create_card(id, title, description, status):
        table.put_item(
            Item={
                'id': id,
                'title': title,
                'description': description,
                'status': status
            }
        )
    
    @staticmethod
    def update_card(id, title, description, status):
        table.update_item(
            Key={'id': id},
            UpdateExpression="set title=:t, description=:d, status=:s",
            ExpressionAttributeValues={
                ':t': title,
                ':d': description,
                ':s': status
            },
            ReturnValues="UPDATED_NEW"
        )
    
    @staticmethod
    def delete_card(id):
        table.delete_item(Key={'id': id})
