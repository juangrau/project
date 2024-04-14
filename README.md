# Data Engineering Project: Where to setup a new Dog Grooming business in NYC

## Problem Description

You want to start a Dog Grooming Business in New York City, but don't know where to set it up in order to be successful. Based on this, you need to know where is the location of the majority of dogs in NYC that have frequent grooming needs, so you aim your business location on a zip code where you can provide service to these dogs.

## Datasets

For this project I found two different dataset that are going to be used combined in order to get the information we need:

### Dog Licenses on New York

**Dataset Description**
All dog owners residing in NYC are required by law to license their dogs. The data is sourced from the DOHMH Dog Licensing System (https://a816-healthpsi.nyc.gov/DogLicense), where owners can apply for and renew dog licenses. Each record represents a unique dog license that was active during the year, but not necessarily a unique record per dog, since a license that is renewed during the year results in a separate record of an active license period. Each record stands as a unique license period for the dog over the course of the yearlong time frame.

**Dataset Location**
The location and further description of this dataset in the following link:
https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp/about_data

### AKCData
**Dataset Description**
Information about 277 dog breeds extracted from the American Kennel Club website using Beautiful Soup.

**Dataset Location**
The location and further description of this dataset in the following link:
https://tmfilho.github.io/akcdata/


In order to make it easier for the project development, I already downloaded both datasets and included them on these links:

- link1
- link2







### Problem statement

Develop a dashboard with two tiles by:
- Selecting a dataset of interest (see Datasets) - ok
- Creating a pipeline for processing this dataset and putting it to a datalake
- Creating a pipeline for moving the data from the lake to a data warehouse
- Transforming the data in the data warehouse: prepare it for the dashboard
- Building a dashboard to visualize the data


## Evaluation Criteria

### Problem description
- 0 points: Problem is not described
- 2 points: Problem is described but shortly or not clearly
- 4 points: Problem is well described and it's clear what the problem the project solves

### Cloud
- 0 points: Cloud is not used, things run only locally
- 2 points: The project is developed in the cloud
- 4 points: The project is developed in the cloud and IaC tools are used

### Data ingestion (choose either batch or stream)
Batch / Workflow orchestration
- 0 points: No workflow orchestration
- 2 points: Partial workflow orchestration: some steps are orchestrated,  some run manually
- 4 points: End-to-end pipeline: multiple steps in the DAG, uploading data to data lake

### Data warehouse
- 0 points: No DWH is used
- 2 points: Tables are created in DWH, but not optimized
- 4 points: Tables are partitioned and clustered in a way that makes sense or the upstream queries (with explanation)

### Transformations (dbt, spark, etc)
- 0 points: No tranformations
- 2 points: Simple SQL transformation (no dbt or similar tools)
- 4 points: Tranformations are defined with dbt, Spark or similar technologies

### Dashboard
- 0 points: No dashboard
- 2 points: A dashboard with 1 tile
- 4 points: A dashboard with 2 tiles

### Reproducibility
- 0 points: No instructions how to run the code at all
- 2 points: Some instructions are there, but they are not complete
- 4 points: Instructions are clear, it's easy to run the code, and the code works