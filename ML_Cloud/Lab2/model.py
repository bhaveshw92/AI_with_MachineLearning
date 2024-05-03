import sagemaker

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Set the IAM role for the SageMaker session
iam_role = sagemaker.get_execution_role()

# Define the container image for the model
image = '683313688378.dkr.ecr.us-east-1.amazonaws.com/sagemaker-xgboost:1.7-1'

# Define the model's S3 location
model_data = 's3://lab2-bucket-bhavesh/output/mk5-training-job/output/model.tar.gz'

# Create the SageMaker model
model = sagemaker.create_model(
    model_name='Lab_2_Model',
    role=iam_role,
    container_defs={
        'Image': image
    },
    vpc_config={
        'Subnets': ['subnet-1', 'subnet-2'],
        'SecurityGroupIds': ['sg-1']
    }
)

# Save the model to your SageMaker account
model.save(sagemaker_session=sagemaker_session)
