import json
import boto3
import pandas as pd
import io

s3_client = boto3.client('s3')
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # Get the bucket and file name from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download the file from S3
    response = s3_client.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read()
    
    # Process the file (convert CSV to JSON)
    df = pd.read_csv(io.BytesIO(data))
    json_data = df.to_json(orient='records')
    
    # Save processed data to another S3 bucket
    output_bucket = 'your-processed-data-bucket'
    output_key = key.replace('input/', 'processed/')
    s3_client.put_object(Bucket=output_bucket, Key=output_key, Body=json_data)
    
    # Send notification
    sns_client.publish(
        TopicArn='arn:aws:sns:your-region:your-account-id:your-topic',
        Message=f'File {key} processed and saved to {output_bucket}/{output_key}',
        Subject='Data Processing Notification'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed successfully!')
    }
