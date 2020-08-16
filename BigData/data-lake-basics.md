# Data Lake Basics
- *Raw or Landing Zone* : Contains the original data ingested into the lake
- *Production or Gold Zone* :  Contains high­ quality, governed data, clean, processed data 
- *Dev or Work Zone*:  The more technical users such as data scientists and data engineers do their work. Once the analytics work performed in the work zone gets productized, it is moved into the gold zone
- *Sensitive Zone*: Contains sensitive data
- Different zones have different levels of governance and service­level agreements

## Data Swamp
A data swamp is a data pond that has grown to the size of a data lake but failed to attract a wide analyst community, usually due to a lack of self­service and governance facilities

## Key steps for creating a Data Lake
- Stand up the infrastructure (get the Hadoop cluster up and running)
- Organize the data lake (create zones for use by various user communities and ingest the data)
- Set the data lake up for self­service (create a catalog of data assets, set up permissions, and provide tools for the analysts to use)
- Open the data lake up to the users

## Setting up Data Lake for Self Service
- Find and Understand
- Provision : Get access to data
- Prepare : clean data and convert it to a format appropriate for analysis
- Analyze : Use the data to answer questions or create visualizations and reports

## Fingerprinting
The tool crawls through all the structured data in the enterprise, adding a unique identifier to each field, and as fields get annotated or tagged by analysts, it looks for similar fields and suggests tags for them.