import json
import boto3
from PIL import Image
import traceback

# AWS Clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Destination bucket
DEST_BUCKET = 'image-processed-divesh'

# SNS Topic ARN
TOPIC_ARN = 'arn:aws:sns:ap-south-1:526545815511:image-processing-alerts'


def lambda_handler(event, context):

    print("========== Lambda Started ==========")
    print("Received Event:")
    print(json.dumps(event))

    try:
        # Get bucket and file details
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        print(f"Source Bucket: {bucket}")
        print(f"Uploaded File: {key}")

        # File paths
        download_path = f'/tmp/{key}'
        upload_path = f'/tmp/resized-{key}'

        print("Downloading image from S3...")

        # Download image
        s3.download_file(bucket, key, download_path)

        print("Image downloaded successfully")

        # Open image
        image = Image.open(download_path)

        print(f"Original Size: {image.size}")

        # Resize image
        image.thumbnail((300, 300))

        print(f"Resized Size: {image.size}")

        # Save resized image
        image.save(upload_path)

        print("Image resized successfully")

        # Upload resized image
        s3.upload_file(
            upload_path,
            DEST_BUCKET,
            f'resized-{key}'
        )

        print(f"Resized image uploaded to {DEST_BUCKET}")

        # Send SNS notification
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject='Image Processed Successfully',
            Message=f'''
Image Processing Completed

Source Bucket: {bucket}
File Name: {key}
Destination Bucket: {DEST_BUCKET}

Status: SUCCESS
            '''
        )

        print("SNS notification sent successfully")

        print("========== Lambda Completed ==========")

        return {
            'statusCode': 200,
            'body': json.dumps('Image processed successfully')
        }

    except Exception as e:

        print("========== ERROR OCCURRED ==========")

        error_message = str(e)

        print("Error:")
        print(error_message)

        print("Traceback:")
        print(traceback.format_exc())

        # Send failure notification
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject='Image Processing Failed',
            Message=f'''
Image Processing Failed

Error:
{error_message}

Check CloudWatch Logs for details.
            '''
        )

        return {
            'statusCode': 500,
            'body': json.dumps('Image processing failed')
        }
