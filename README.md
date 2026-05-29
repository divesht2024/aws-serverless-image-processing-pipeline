# 🚀 AWS Serverless Image Processing Pipeline

An end-to-end **serverless, event-driven AWS architecture** that automatically processes uploaded files, sends notifications, and provides full observability using CloudWatch.

---

## 📌 Architecture Overview

This project implements a fully automated pipeline:

**S3 Upload → Lambda Processing → SNS Notification → CloudWatch Monitoring**

---

## 🧠 Key Features

### 🔥 Event-Driven Architecture
- Upload file to S3 triggers automatic Lambda execution
- No manual intervention required
- Fully automated workflow

### ⚙️ Serverless Compute
- AWS Lambda handles image/file processing
- Scales automatically based on demand

### 🔔 Decoupled Notifications
- Amazon SNS sends email alerts on successful processing
- Loose coupling between services

### 📊 Observability & Monitoring
- CloudWatch Logs for debugging
- CloudWatch Metrics for performance tracking
- Alarm notifications for failures/success tracking

---

## 🏗️ AWS Services Used

| Service | Purpose |
|--------|--------|
| Amazon S3 | File storage (input/output buckets) |
| AWS Lambda | Serverless processing engine |
| Amazon SNS | Email notifications |
| Amazon CloudWatch | Logging, metrics, alarms |

---

## 🔄 Workflow

1. User uploads image/file to **S3 Input Bucket**
2. S3 event triggers **AWS Lambda function**
3. Lambda processes the file (resize/transform/etc.)
4. Output saved to **S3 Output Bucket**
5. SNS sends success notification
6. CloudWatch logs and monitors entire flow

---

## 📂 Project Structure
│
├── lambda/
│ ├── index.py # Main Lambda function
│ ├── requirements.txt # Dependencies (Pillow, etc.)
│
├── test-data/
│ ├── sample-image.jpg # Test input files
│
├── screenshots/
│ ├── s3-upload.png
│ ├── lambda-success.png
│ ├── sns-email.png
│ ├── cloudwatch-logs.png
│
├── architecture/
  ├── 
  ├── 
├── README.md

---

⚙️ Setup Instructions
1️⃣ Create S3 Buckets
Create:
Input bucket
Output bucket

Example:
image-upload-bucket
processed-image-bucket


2️⃣ Create Lambda Function
Runtime: Python 3.x
Add S3 PUT trigger
Configure IAM permissions
Required permissions:
Amazon S3 access
CloudWatch Logs access
SNS publish access


3️⃣ Install Dependencies
Inside requirements.txt
Pillow==10.3.0
Install locally:
pip install -r requirements.txt


4️⃣ Configure SNS
Create SNS Topic
Add email subscription
Confirm email subscription


5️⃣ Enable Monitoring
Use CloudWatch Logs for Lambda execution tracking
Create CloudWatch alarms for failures/errors

---

📊 What This Project Demonstrates
Event-driven architecture
AWS serverless computing
Cloud automation workflows
Monitoring and observability
Production-style AWS integration
Decoupled cloud design


---

🚀 Future Enhancements
Multiple image resizing formats
DynamoDB integration
API Gateway upload endpoint
CI/CD pipeline with GitHub Actions
Infrastructure as Code using Terraform

---

👨‍💻 Author

Divesh M. Tayade
AWS Cloud & DevOps Enthusiast
