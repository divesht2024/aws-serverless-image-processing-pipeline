# 🏗️ Architecture Diagram

This folder contains the architecture diagram for the AWS Serverless Image Processing Pipeline project.

## 📌 Architecture Flow

```text
User Uploads File
        ↓
Amazon S3 (Input Bucket)
        ↓
AWS Lambda Trigger
        ↓
Image/File Processing
        ↓
Amazon S3 (Output Bucket)
        ↓
Amazon SNS Notification
        ↓
Amazon CloudWatch Logs & Monitoring
```

