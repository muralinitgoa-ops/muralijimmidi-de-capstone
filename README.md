# DE Capstone Project
This is my AWS Data Engineering Practice Project
# AWS Data Engineering Upskilling

## Week 2 – Data Modeling and Analytics (Python + SQLite)

In Week 2 we built a small taxi analytics system using Python and SQLite.

### Database Setup
Created a SQLite database:


Created normalized tables:

- zones
- vendors
- trips

### Tables

zones  
zone_id | zone_name

vendors  
vendor_id | vendor_name

trips  
trip_id | vendor_id | pickup_zone | dropoff_zone | trip_distance | trip_duration | trip_date

### Sample Data
Inserted taxi trip data for analysis.

### Analytics Performed

1. Total number of trips
2. Average trip distance
3. Average trip duration
4. Trips per vendor
5. Trips per zone
6. Longest trip distance
7. Shortest trip distance
8. Total distance travelled per vendor
9. Average trip duration per vendor
10. Trips per day

These analytics were implemented using SQL queries executed through Python.

### Week 2 Notebook

Google Colab notebook for Week-2 implementation:

https://colab.research.google.com/drive/1Vzghmyyo3UKheagnm0mCfslzJsyWwhCo

---

# Week 3 – AWS Data Lake Implementation

### S3 Data Lake

Created an AWS S3 bucket:
de-upskilling-data-lake-murali

Folder structure:
raw/
staging/
curated/


### Lifecycle Policy

Configured lifecycle rule to move objects to **Standard-IA after 30 days**.

### Dataset Upload

Uploaded taxi dataset using AWS CLI via CloudShell.

Example command:
aws s3 ls s3://de-upskilling-data-lake-murali/raw/


### Python boto3 Test

Created a Python script to interact with S3 using boto3 SDK.

### CloudTrail Logging

Enabled CloudTrail to log AWS account activity.

### CloudWatch Monitoring

Created a CloudWatch dashboard to monitor S3 API metrics.

### Budget Monitoring

Configured AWS Budget to monitor spending and prevent unexpected charges.

---

### Architecture
Python ETL
↓
SQLite Database
↓
AWS S3 Data Lake
↓
CloudTrail Logging
↓
CloudWatch Monitoring
↓
AWS Budget Cost Control
