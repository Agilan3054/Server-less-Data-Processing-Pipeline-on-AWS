# Serverless Data Processing Pipeline on AWS

This project involves the development of a serverless data processing pipeline using AWS Lambda to automatically process and transform data uploaded to Amazon S3. The pipeline leverages AWS Glue for ETL operations, Amazon Athena for querying processed data, and Amazon SNS for real-time notifications.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Setup](#setup)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Introduction
The serverless data processing pipeline aims to streamline the ingestion, processing, and analysis of data using AWS services. By leveraging AWS Lambda, AWS Glue, Amazon Athena, and Amazon SNS, the pipeline ensures efficient, scalable, and automated data processing and analysis.

## Features
- Serverless data processing using AWS Lambda.
- Automated ETL operations with AWS Glue.
- Scalable data analysis with Amazon Athena.
- Real-time notifications using Amazon SNS.
- Efficient and automated data processing pipeline.

## Architecture
The system architecture includes the following components:
1. **AWS Lambda**: For serverless processing and transformation of data uploaded to Amazon S3.
2. **AWS Glue**: For ETL operations, cataloging, and transforming data.
3. **Amazon S3**: For storing raw and processed data.
4. **Amazon Athena**: For running SQL queries on processed data.
5. **Amazon SNS**: For real-time notifications upon data processing completion.

## Setup
### Prerequisites
- AWS account
- AWS CLI configured
- IAM roles with necessary permissions for AWS Lambda, AWS Glue, Amazon S3, Amazon Athena, and Amazon SNS

### Installation

1. Deploy the AWS Lambda function:
    - Create a Lambda function in the AWS Management Console or using AWS CLI.
    - Upload the Lambda function code (`lambda_function.py`).

2. Configure S3 bucket:
    - Create an S3 bucket to store raw and processed data.
    - Update the S3 bucket name in the Lambda function code and AWS Glue script.

3. Set up AWS Glue:
    - Create a Glue crawler to catalog the data.
    - Create a Glue job for the ETL process, using the provided script (`glue_etl_script.py`).

4. Configure Amazon Athena:
    - Set up Athena to query the processed data stored in S3.

5. Set up Amazon SNS:
    - Create an SNS topic for real-time notifications.
    - Update the SNS topic ARN in the Lambda function code.

## Usage
1. **Uploading Data**:
    - Upload data to the configured S3 bucket.
    - The Lambda function will automatically trigger, processing and transforming the data.

2. **ETL Operations**:
    - AWS Glue will catalog and transform the data, storing the results back in S3.

3. **Querying Data**:
    - Use Amazon Athena to run SQL queries on the processed data stored in S3.

4. **Real-Time Notifications**:
    - Amazon SNS will send real-time notifications upon data processing completion.

## Technologies Used
- **AWS Lambda**: For serverless data processing.
- **AWS Glue**: For ETL operations.
- **Amazon S3**: For data storage.
- **Amazon Athena**: For data querying.
- **Amazon SNS**: For real-time notifications.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

