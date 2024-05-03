import boto3

# Create an S3 client
s3 = boto3.client('s3', region_name='us-east-1')

# List all the bucket names
response = s3.list_buckets()
bucket_names = [bucket['Name'] for bucket in response['Buckets']]

print(bucket_names)

# Create an EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Call the describe_instances method to list all the EC2 instances in your account
response = ec2.describe_instances()

# Get a list of all the instances
instances = response['Reservations']

# Iterate through the list and print the instance ID, instance type, and state for each instance
for instance in instances:
    instance_id = instance['Instances'][0]['InstanceId']
    instance_type = instance['Instances'][0]['InstanceType']
    instance_state = instance['Instances'][0]['State']['Name']
    print(f'Instance ID: {instance_id}, Instance Type: {instance_type}, State: {instance_state}')