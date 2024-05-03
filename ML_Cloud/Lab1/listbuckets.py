import boto3

# Create an S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# List all the bucket names
response = s3.list_buckets()
bucket_names = [bucket['Name'] for bucket in response['Buckets']]

print(bucket_names)
