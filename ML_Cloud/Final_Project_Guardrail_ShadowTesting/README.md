# ML in Cloud Final Project: Deployment Guardrail and Shadow Testing in SageMaker

## Background
Direct marketing, either through mail, email, phone, etc., is a common tactic to acquire customers. Predicting those potential customers based on readily available information like demographics, past interactions, and environmental factors is a common machine learning problem. This project focuses on training a model to predict if a customer will enroll for a term deposit at a bank, after one or more phone calls. Hyperparameter tuning will be used to try multiple hyperparameter settings and produce the best model. Use Deployment Guardrail and Shadow Testing for traffic Shifting implementation.

## Preparation
- Specify the S3 bucket and prefix for training and model data.
- Define the IAM role for accessing data.

## Notebook (1): Traffic Shifting Simulation
- Simulate a successful deployment and a failure in an update.
- Download two model artifacts and upload them to S3.
- Create three models from the artifacts, including one incompatible model for error simulation.

## Notebook (2): Endpoint Configuration
- Create endpoint configurations for each model.

## Endpoint Deployment and Metrics
- Deploy the first endpoint and test its metrics.
- Create CloudWatch alarms for Invocation 5XX Errors and Model Latency.
- Update the endpoint to use a new configuration and pass "BlueGreenUpdatePolicy".
- Trigger alarms during the update process.

## Notebook (3): Auto Rollback
- Demonstrate automatic rollback due to failure.

## Notebook (4): Successful Deployment
- Deploy the model successfully without triggering alarms.

## SageMaker Shadow Testing
- Utilize SageMaker Shadow Testing to compare the performance of a new model version with the current one.
- Create a new test with production and shadow variants.
- Observe and analyze metrics from the shadow test.
- Mark the test as complete and choose the appropriate action for the shadow variant.

## Rules and Conditions
- Use the specified data set and models for the project.
- Train two models using SageMaker Hyperparameter Tuning.
- Simulate a failed deployment and a successful deployment using Deployment Guardrail.
- Utilize SageMaker Shadow Testing to compare model variants and allow the shadow variant to replace the production variant.

For detailed implementation steps and code, refer to the notebooks and scripts provided in the project repository.
