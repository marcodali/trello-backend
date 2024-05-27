import boto3

dynamodb = boto3.resource('dynamodb', region_name='ca-central-1')
table = dynamodb.Table('Cards')

# Consulta utilizando el GSI
response = table.query(
    IndexName='StatusIndex',
    KeyConditionExpression=boto3.dynamodb.conditions.Key('status').eq('Done')
)

# Imprimir los ítems obtenidos
for item in response['Items']:
    print(item)
