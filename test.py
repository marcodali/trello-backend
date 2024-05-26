import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

try:
    dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')
    table = dynamodb.Table('Cards')
    
    # Verificar las credenciales
    client = boto3.client('sts')
    identity = client.get_caller_identity()
    print("Current AWS Identity:", identity)
except (NoCredentialsError, PartialCredentialsError) as e:
    print("Error de credenciales:", e)
except Exception as e:
    print("Error al conectarse a DynamoDB:", e)
