# Lab: SageMaker GroundTruth Text Classification

## Assignment Description:

1. Upload the customer feedback data stored in a CSV file (e.g., customer_feedback.csv) to an S3 bucket.
2. Create a new folder within the S3 bucket to serve as the output location for the labeled data.
3. Set up a labeling job in Amazon SageMaker GroundTruth:
   - Specify the source and destination S3 buckets for input and output data.
   - Define the role and data type for the labeling job.
   - Complete the data setup process.
4. Review the manifest file generated by SageMaker GroundTruth.
5. Configure the labeling job for Text Classification (Single Label).
6. Specify a private group, add a group name, and invite yourself to label the jobs.
7. Check your email for a temporary password, login to SageMaker GroundTruth, change the password, and log in again.
8. Confirm your email in the Labeling workforce.
9. Wait for approximately 10 minutes to see the labeling job appear in the SageMaker GroundTruth console.
10. Label the semantic of the customer feedbacks as per the assigned task.
11. Check the labeled data in the designated output folder within the S3 bucket and verify it in the SageMaker GroundTruth console.

## Notes:

- Ensure that the customer feedback data is uploaded to the S3 bucket in CSV format and organized properly.
- Follow the step-by-step instructions provided to set up the labeling job in SageMaker GroundTruth.
- Verify the completion of each task before proceeding to the next step to avoid errors.
- Monitor the labeling job status in the SageMaker GroundTruth console and wait for the job to appear if it does not show up immediately.
- Check the output folder in the S3 bucket to access the labeled data once the labeling job is completed.
- Follow the steps given in 'Using SageMaker.pdf'.