import boto3

def lambda_handler(event, context):
    # Initialize S3 client and Translate client
    s3 = boto3.client('s3')
    translate = boto3.client('translate')

    # Get the source bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_object_key = event['Records'][0]['s3']['object']['key']

    # Download the object from the source bucket
    response = s3.get_object(Bucket=source_bucket, Key=source_object_key)
    source_text = response['Body'].read().decode('utf-8')

    # Translate the text
    result = translate.translate_text(
        Text=source_text,
        SourceLanguageCode='auto',  # Source language code (e.g., English)
        TargetLanguageCode='hi'   # Target language code (e.g., Hindi)
    )

    translated_text = result['TranslatedText']

    # Upload the translated result to the destination bucket
    destination_bucket = 'lab3-sagemaker-output'  # Replace with actual destination bucket name
    destination_object_key = f'translated/{source_object_key}'  # Modify the key as needed
    s3.put_object(Body=translated_text.encode('utf-8'), Bucket=destination_bucket, Key=destination_object_key)

    return {
        'statusCode': 200,
        'body': 'File translated and result uploaded successfully!'
    }
