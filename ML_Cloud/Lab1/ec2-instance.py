import boto3

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