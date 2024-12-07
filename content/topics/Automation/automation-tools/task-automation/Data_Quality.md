---
title: "Data Quality Evaluation"  
description: " This content explains the importance of the Data Quality evaluation in data pipeline and implementing of Data Quality evaluation by use of Dataplex on Google Cloud Platform."  
keywords: "Data Quality, Data Pipeline, Dataplex, GCP"  
date:  
weight:  
author: "Kheiry Sohooli"  
authorlink: "https://tilburgsciencehub.com/contributors/kheirysohooli"  
---

## Overview

Data quality (DQ) used to just focus on giving data consumers good data, but now it's about making sure an organization can check how accurate its data is and understand the effects of using data with different levels of accuracy while still meeting the needs of the data consumer. Based on the definition provided, data quality evaluation aims to assess the accuracy and reliability of data and make it visible to the data consumer. It seeks to understand the tradeoffs involved in using data at different levels of correctness to ensure that it is useful and relevant throughout its lifecycle. In this article, after briefly reviewing the concepts of DQ, Dataplex is introduced as a tool to evaluate DQ automatically on the Google Cloud Platform(GCP). You'll learn how to assess data quality with Dataplex by creating and running a data quality scan using predefined rules.

## The Importance of Data Quality

Managing data quality is crucial for improving data analytics in businesses. High-quality data is essential for making informed business decisions and governing data within an organization. By evaluating data againste a set of rules and addressing the low quality data, organizations can find and fix problems like duplicate data, missing values, outliers, and any other issues relevant to a business. Data quality tools provide value by helping organizations to find underlying data issues quickly and effectively. The data that are not qualified will not be transferred to the next step, and its propagation to the pipeline will be halted. This data would be determined, and the data owner responsible for curing it can solve the issues with the data if possible. Also, by finding the problem with the data ingested, it is possible to see the trend of the problem and the source of the issue, then it could avoid it. 

When data meets standards for quality—such as accuracy, completeness, consistency, timeliness, validity, and uniqueness—and the results are shared with consumers, they can decide whether to use the data without further evaluation. This autonomy improves agility and supports more accurate decision-making.

The quality check can be performed immediately after data ingestion to ensure it aligns with the required rules. Additionally, the check can also be carried out after any transformation processes to obtain information about the data's quality and adherence to the rules. This is particularly important in decentralized environments where data prepared by one domain is consumed by another. 

## Data Quality Specification
A data quality specification defines the expectations for data. These logical expectations must be converted into JSON format to be machine-readable. The key qualities evaluated depend on the organization’s policies and the nature of the data. However, two main aspects are typically checked:

Schema: This is the most common criterion for structured data. It includes the data structure, data types, and column names.

Semantics: This refers to the logical business rules applied to the data. For example, a customer’s contract number should have exactly 10 digits.

## Dataplex 

Dataplex is an intelligent data fabric on GCP that enables organizations to centrally discover, manage, monitor, and govern their data across data lakes, data warehouses, and data marts to power analytics at scale. 

One of the features in Dataplex is DQ evaluation. The advantages of DQ evaluation using Dataplex are : 

1- Dataplex provides **data profiling** capabilities that offers insights into dimensions like completeness, accuracy, validity, consistency. 

{{% tip %}}
Data profiling delivers richer insight into the data by identifying its common statistical characteristics. Learn more about data profiling [here](https://cloud.google.com/dataplex/docs/data-profiling-overview). 
{{% /tip %}}

2- The scan results can be integrated with some resources like BigQuery and Looker (for visualization).

3- A valuable feature of DQ evaluation by Dataplex is the ability to define a data quality task and connect it to any number of BigQuery tables and Cloud Storage files. Using Dataplex data quality tasks, you can integrate data quality checks into everyday workflows by validating data that is part of a data production pipline, regularly monitoring the quality of your data against a set of criteria, and building data quality reports.

## Step by Step DQ Enforcement
In this article, the procedure for evaluating the data quality of a structured dataset is demonstrated by implementing the section highlighted in the red rectangle in the following design pattern.
<p align = "center">
<img src = "../images/DQScan.png" width="500">
</p>


### 1- Preparation Steps 

Start by creating a new GCP project after [signing in to GCP.](https://console.cloud.google.com/home/dashboard?project=wide-factor-416710). 

- Create a new project and give it a name, such as "Data Quality Validation". Select your organization, click Create, and ensure the new project is selected in your environment.

<p align = "center">
<img src = "../images/Create_new_project.png" width="500">
</p>

- Activate the Cloud Shell to manage your project, located at the top right of the Cloud Console.

<p align = "center">
<img src = "../images/Cloud_Shell.png" width="500">
</p>

- Run `gcloud config set project "Project_ID"` in Cloud Shell, replacing "Project_ID" with your actual project ID.

- Authorize access to your project resources when prompted in the pop-up window. 

{{% tip %}}
Google offers a 90-day trial with a €300 credit to use. For more information, click [here](https://cloud.google.com/free/docs/free-cloud-features).
{{% /tip %}}


### 2- Datasets managements

- In the navigation menu, go to **Analytics** and select **Dataplex**. If you see a prompt that says "Welcome to the new Dataplex experience," click **Close**.

- In the left sidebar, under **Manage Lakes**, click on **Manage** and then select **Create**. Enter a name for your new lake and leave the other settings at their default values. Click **Create** to proceed. You can name it "walmart"(In this project, we use a Walmart dataset from [Kaggle](https://www.kaggle.com/datasets/yasserh/walmart-dataset)).

It may take up to 5 minutes to create a new lake.

- To create a zone, click on the name of your lake, then click the "+" button to add a zone. Enter a name for the zone, leave the other parameters as default, and click **Create**. You can name it "Sale".

- Next, add an asset to the zone. Click on the name of your zone, then click **Add Asset** and select **Add an Asset**. In the right panel, fill in the data specifications. You can add a data asset from either a BigQuery table or a Google Cloud Storage (GCS) bucket. Choose the option where your data is located.

  Once you have entered the required information, click **Done**, then **Continue**. For Discovery settings, select **Inherit** to use the zone-level settings, and click **Continue**. Finally, click **Submit**.

<p align = "center">
<img src = "../images/Add_Asset.png" width="500">
</p>

{{% tip %}}
To add your data to GCS, go to the navigation menu, select **Cloud Storage**, then **Bucket**. Create a bucket with a unique name and upload your data there. Ensure that your bucket and zone are in the same region.
{{% /tip %}}

- Finally, create an empty dataset to store Data Quality (DQ) results. In the BigQuery interface, go to the `Explorer` panel, expand the **Actions** menu for your project, and click **Create Dataset**. Provide a unique name for the dataset within your project and specify the region, ensuring it matches the region of your previously defined zone. Click **Create Dataset** to finish.


### 3- Create Data Quality Scan Job
Navigate to Dataplex and go to the Dataplex interface. In the left panel, select **Govern** and then click on **Data Quality** > **Create Data Quality Scan**.
The process of creating a scan job involves three steps:

#### 1- Define the Scan Job:

In this step, you will need to provide a name for the scan job, select your dataset, and create a `profile scan`.

- You can choose to run the quality scan on-demand, schedule it at regular intervals, or set it to run automatically after new data is ingested.

- Specify the scope of the scan job.

{{% tip %}} in `Scope` field you can opt to scan all data or a specific subset of data. {{% /tip %}}
<p align = "center">
<img src = "../images/QRule_1.png" width="500">
</p>

#### 2- Set Data Quality Rules:

In Dataplex, you have five options for defining data quality rules:

- Profile-Based Rules: Dataplex scans the data, derives information, and sets rules for each column automatically.

- Built-in Rules: These are standard rules applicable to most datasets (e.g., Null check, Range check, Uniqueness check, Regex check).

- SQL Row Check Rule: Select a quality dimension and column, set a threshold for passing/failing based on the number of rows that do not meet the criteria. Useful for defining semantic rules.

- SQL Aggregate Check Rule: Similar to the SQL Row Check, but focuses on aggregation properties of the column rather than individual rows. Useful for semantic checks at an aggregated level.

- SQL Assertion Rule: Specify a column and quality dimension, then use an SQL statement to validate the data. If any rows are returned, the rule fails. Useful for checking semantic rules.

<p align = "center">
<img src = "../images/Qulity_rules.png" width="500">
</p>

This guide focuses on built-in rules as they are easy to start with and applicable to many organizational needs. After selecting a rule, choose the columns you want to check and apply the relevant rule to each column.

<p align = "center">
<img src = "../images/QRule_2.png" width="500">
</p>

The above image shows a scan job where the Completeness dimension of several columns is checked by verifying for null values.


#### 3- Select the Dataset for Scan Results:

Choose the dataset where you want to store the scan results.

<p align = "center">
<img src = "../images/QRule_3.png" width="500">
</p>

Click **Create**. It will take a few minutes to set up. Once created, click on the job to run the scan.

Clicking on the Data Quality job will show three sections: a review section, a data quality scan configuration, and a table view with job status, history, permissions, and logs. You can use filters to view specific logs, such as warnings.
<p align = "center">
<img src = "../images/Passed_Completeness.png" width="500">
</p>

After the scan job runs, results are stored in the assigned dataset. For detailed job results, view the output in the BigQuery table specified in the last step. You can connect this table to `Looker` for visualizing results and aggregating multiple scans. This is useful for sharing data quality insights with other teams, enhancing trust in data. Additionally, by analyzing aggregated quality scans, you can identify error trends and address issues at their source.

<p align = "center">
<img src = "../images/quality_results.png" width="500">
</p>



{{% tip %}}
By enabling data cataloging, data quality results will be added to your dataset's metadata in the data catalog. There, you can view a summary of the scan results and access a link to a BigQuery table or Looker to see detailed results and visualize them. The information on the Data Catalog is highlighted by a blue rectangle in the design pattern image.
{{% /tip %}}

{{% tip %}}
By using the logs generated for each job in Dataplex, you can receive alerts when necessary. You can set alerts for data quality failures to be sent to the data owner.
{{% /tip %}}

{{% summary %}}

This article covers the following topics:

- An introduction to data quality (DQ) evaluation and its importance

- DQ specifications, including rules and expectations used for evaluating data

- An introduction to Dataplex

- A step-by-step guide for implementing data quality checks

{{% /summary %}}