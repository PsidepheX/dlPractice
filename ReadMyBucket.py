import boto3
import pandas

client = boto3.client(
    's3',
    aws_access_key_id = 'AKIAVKK7A55OF7H3TXBQ',
    aws_secret_access_key = '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',
    region_name = 'us-east-2'
)
    
resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIAVKK7A55OF7H3TXBQ',
    aws_secret_access_key = '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',
    region_name = 'us-east-2'
)

obj = client.get_object(
    Bucket = 'dustinsbucket',
    Key = 'I want to say'
)
    
data = pandas.read_csv(obj['Body'])
    
print('Printing the data frame...')
print(data)
