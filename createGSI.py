import boto3

# Crear una instancia del cliente de DynamoDB
dynamodb = boto3.client('dynamodb', region_name='ca-central-1')

# Nombre de la tabla
table_name = 'Cards'

# Modificar la tabla para agregar el GSI con todos los atributos
response = dynamodb.update_table(
    TableName=table_name,
    AttributeDefinitions=[
        {
            'AttributeName': 'status',
            'AttributeType': 'S'
        },
    ],
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'StatusIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'status',
                        'KeyType': 'HASH'  # Clave de partición
                    },
                ],
                'Projection': {
                    'ProjectionType': 'ALL'  # Incluir todos los atributos
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            }
        },
    ]
)

print("Índice GSI creado:", response)
