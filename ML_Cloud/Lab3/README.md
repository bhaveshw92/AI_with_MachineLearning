# Lab 2: AWS AI Service Integration with Lambda Function

## Assignment: Integrating Translate Service with Lambda Function

### Task Description:

1. Upload an appropriate file to the "source" S3 bucket, depending on the target AI service (e.g., text file for translation, image file for text detection).
2. Configure a Lambda function to be triggered by S3 events upon object upload to the "source" bucket.
3. Write Lambda function code to extract the location of the uploaded object in the S3 bucket.
4. Utilize the Translate service to translate text from the uploaded file.
5. Save the result of the translation (or other AI service) to the "destination" S3 bucket or print it in the Lambda function console.
6. Ensure that the source and destination buckets are different to avoid overwriting the original data.

### Notes:

- Ensure that the Lambda function has appropriate permissions to access the Translate service and both source and destination S3 buckets.
- Customize the Lambda function code to handle specific AI services and file formats based on the chosen task (e.g., translation, text detection, sentiment analysis).
- Test the Lambda function with S3 event triggers to validate its functionality.
- Maintain separation between source and destination buckets to preserve original data and avoid data loss or corruption.
- The file 'translate.py' was use to as a lambda function to inetiate the translate service. 
