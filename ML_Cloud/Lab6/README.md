# Lab: Training a Model with Amazon SageMaker

## Task Description:

1. Explore the built-in algorithms provided by Amazon SageMaker listed in the [documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html).
2. Select an algorithm other than KNN that you are comfortable with for training a model.
3. Choose an appropriate dataset from [OpenML](https://www.openml.org/) or [Kaggle](https://www.kaggle.com/) - Same as previous lab and continue training.
4. Complete the training job and store the model artifact in the S3 bucket.
5. Upload the selected dataset and the notebook file used for training the model to Blackboard (BB).

## Implementation Steps:

1. Algorithm Selection:
   - Chose LinearLerner for training the model.

2. Dataset Selection:
   - Selected the Stroke Predection from [OpenML/Kaggle].

3. Model Training:
   - Utilized Amazon SageMaker to train the model using the selected algorithm and dataset.
   - Completed the training job and stored the model artifact in the specified S3 bucket.

4. File Upload:
   - Uploaded the selected dataset and the notebook file used for model training to Blackboard (BB).

## Notes:
- Ensure not to start a hosting job to avoid unnecessary credit consumption.
- If a hosting endpoint is accidentally initiated, remember to terminate it promptly.

## Conclusion:
- Successfully completed the assignment by selecting an appropriate algorithm, dataset, and performing model training using Amazon SageMaker.
