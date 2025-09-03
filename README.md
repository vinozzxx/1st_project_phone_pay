# Project phonepe

**PhonePe Pulse**  Transaction Insights – Data Analysis & Visualization Project

## Project Description
This project leverages the PhonePe Pulse Dataset to explore, analyze, and visualize digital transaction trends across India. The insights are drawn from various dimensions such as state-wise transaction patterns, device usage behavior, insurance penetration, and user engagement over time.

The goal of this project is to extract meaningful business insights that can support decision-making for marketing, expansion, and user engagement strategies.

The Indian digital payments story has truly captured the world’s imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by mobile phone penetration, internet access, and state-of-the-art payments infrastructure.

PhonePe, launched in 2016, has played a significant role in this transformation. As a way to give back to the data and developer community, PhonePe released the PhonePe Pulse Dataset API, which is licensed under [CDLA-Permissive-2.0 open data license](https://github.com/PhonePe/pulse/blob/master/LICENSE), — an open data initiative to demystify digital payments in India.

## Table of Contents
- [Project Description](#project-description)
- [Dataset Insight](#dataset-insight)
- [Tech Stack](#tech-stack)
- [Key Features](#key-features)
- [Documentation](#documentation)
- [Folder Structure](#folder-structure)
- [Structure Breakdown](#structure-breakdown)
- [File Naming](#file-naming)
- [Example Folder Structure](#example-folder-structure)
- [Data Extraction Aggregated Insurance](#data-extraction-aggregated-insurance)
  - [How it works](#how-it-works)
  - [Example Code Snippet](#example-code-snippet)
  - [JSON Structure (Sample)](#json-structure-sample)
- [Dashboard](#PhonePePulseDataAnalysis&Dashboard)
- [Project Structure](#project-structure)
- [FAQs](#faqs)
---
**[`^        back to top        ^`](#Project-phonepe)**

## Goal
The goal of this project is to analyze and visualize the PhonePe Pulse dataset to uncover insights into digital payment trends across India.

## Guide

Follow these steps to explore the dataset:

1. Clone the repository
2. Navigate to the data folder
3. Use Python scripts to extract insights
**[`^        back to top        ^`](#Project-phonepe)**

## Dataset Insight

This project focuses on analyzing digital transaction trends across India using the PhonePe Pulse dataset. It includes:
- Analyze transaction behavior across states, quarters, and payment categories.
- Understand user engagement across device brands and app usage.
- Explore insurance transaction growth and regional adoption.
- Build a dashboard for interactive data visualization and business insights.
**[`^        back to top        ^`](#Project-phonepe)**
  
##  Tech Stack
- [**Python**](https://www.python.org/) – Data analysis and visualization
- [**PostgreSQL**](https://www.postgresql.org/) – Data storage and querying
- [**Pandas**](https://pandas.pydata.org/), [**Plotly**](https://plotly.com/), [**Matplotlib**](https://matplotlib.org/) – Data manipulation and plotting
- [**Streamlit**](https://docs.streamlit.io/) – Dashboard development
- [**GeoJSON**](https://geojson.io/#map=2/0/20) – Mapping state boundaries for choropleth maps
**[`^        back to top        ^`](#Project-phonepe)**
  
##  Key Features

-  Bar, line, and pie charts of transaction data
-  Choropleth map showing state-wise transaction values
-  Filters for Year and Quarter selection
-  Top-performing states displayed dynamically
-  Business insights and KPIs visualized
 **[`^        back to top        ^`](#Project-phonepe)**

## Documentation

### Folder Structure

Navigate to the `data` folder to explore the following structure. The top-level folders include sections for:
- **Aggregated Data**
- **Map Data**
- **Top Data**

Each of these sections contains subfolders for:
- `transaction`
- `user`
- `insurance`
**[`^        back to top        ^`](#Project-phonepe)**
  
#### Structure Breakdown:
- The data is organized at two levels: **Country** and **State**.
- Inside the `country/india` folder, data is grouped by **year** (e.g., 2018, 2019, etc.).
- Similarly, the `state` folder contains subfolders for each **state** in India, also grouped by **year**.

#### File Naming:
- Each year folder (both for country and state) includes **up to four JSON files**:
  - `1.json`, `2.json`, `3.json`, `4.json`
  - These represent **Quarter 1 to Quarter 4** of that year.

---
**[`^        back to top        ^`](#Project-phonepe)**

### Example Folder Structure:

```plaintext
data/
├── aggregated/
│   ├── transaction/
│   │   └── country/
│   │       └── india/
│   │           ├── 2018/
│   │           │   ├── 1.json
│   │           │   ├── 2.json
│   │           └── state/
│   │               └── tamil-nadu/
│   │                   ├── 2018/
│   │                   │   ├── 1.json
│   │                   │   └── 2.json
│   ├── user/
│   └── insurance/

```
**[`^        back to top        ^`](#Project-phonepe)**

...
## Data Extraction Aggregated Insurance:
The following Python code extracts aggregated insurance data at the state level from the PhonePe Pulse dataset. It navigates through nested directories and reads JSON files representing different years and quarters.

# How it works:
Navigates through this folder path:
[data](https://github.com/PhonePe/pulse/tree/master/data)/[aggregated](D:\Studys\GUVI\Project_Phone_Pay\pulse\data\aggregated)/insurance/[country](D:\Studys\GUVI\Project_Phone_Pay\pulse\data\aggregated\insurance\country\india)/india/state/{state}/{year}/{quarter}.json

Extracts:
-[State](D:\Studys\GUVI\Project_Phone_Pay\pulse\data\aggregated\insurance\country\india\state)
-[Year](D:\Studys\GUVI\Project_Phone_Pay\pulse\data\aggregated\insurance)
-[Quarter](D:\Studys\GUVI\Project_Phone_Pay\pulse\data\aggregated\insurance\country\india\2020)
-Transaction Type
-Transaction Count
-Transaction Amount

**[`^        back to top        ^`](#Project-phonepe)**


# Example Code Snippet:
```plaintext
#Required libraries
import pandas as pd
import json
import os

#Path to the state-wise data folder
agg_state_path = r".../data/aggregated/insurance/country/india/state"
agg_state_list = os.listdir(agg_state_path)

#Create an empty dictionary to collect the data
agg = {
    'State': [], 'Year': [], 'Quarter': [],
    'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []
}

#Read JSON files and extract data
for state in agg_state_list:
    state_path = os.path.join(agg_state_path, state)
    for year in os.listdir(state_path):
        for qtr in os.listdir(os.path.join(state_path, year)):
            json_path = os.path.join(state_path, year, qtr)
            if json_path.endswith(".json"):
                with open(json_path, 'r') as file:
                    data = json.load(file)
                for entry in data['data']['transactionData']:
                    agg['State'].append(state)
                    agg['Year'].append(year)
                    agg['Quarter'].append(int(qtr.strip('.json')))
                    agg['Transaction_type'].append(entry['name'])
                    agg['Transaction_count'].append(entry['paymentInstruments'][0]['count'])
                    agg['Transaction_amount'].append(entry['paymentInstruments'][0]['amount'])

#Convert to DataFrame
Agg_insurance_state = pd.DataFrame(agg)
```

## JSON Structure (Sample)
```plaintext
Sample file path:
data/aggregated/insurance/country/india/state/delhi/2018/1.json
Sample JSON:
json
{
  "success": true,
  "code": "SUCCESS",
  "data": {
    "from": 1514745000000,
    "to": 1522175400000,
    "transactionData": [
      {
        "name": "Health Insurance",
        "paymentInstruments": [
          {
            "type": "TOTAL",
            "count": 150000,
            "amount": 350000000.00
          }
        ]
      },
      ...
    ]
  },
  "responseTimestamp": 1630346628866
}
```
...

## 📊 PhonePe Pulse Data Analysis & Dashboard

![PhonePe Dashboard ScreenShort](https://github.com/vinozzxx/1st_project_phone_pay/blob/745665f074cd07e83fce9a3f51f4a3486b53ac9e/Screenshot%20(29).png)

**[`^        back to top        ^`](#Project-phonepe)**

## 📁 Project Structure

```bash
📁 1st_project_phone_pay/
│
├── 📂 Documentation/            # Processed data or user guides (optional)
├── 📂 sql/                      # SQL queries or .sql files
│   └── (unzipped .sql files)     # Unzip sql.zip for easy access
├── 📄 README.md                 # Project overview and instructions
├── 📄 app.py                    # Streamlit dashboard app file
├── 📄 project.ipynb             # Jupyter Notebook with analysis steps
└── 📄 phonepe_dashboard.py      # Main Streamlit dashboard file
```
**[`^        back to top        ^`](#Project-phonepe)**

## FAQs
1. `What is this project about?`
This project analyzes and visualizes PhonePe Pulse data using Python, PostgreSQL, and Streamlit. It extracts data from JSON files, stores it in a database, and presents insights through an interactive dashboard.

2. `Where is the data sourced from?`
The data is sourced from the official PhonePe Pulse GitHub Repository, which contains quarterly transaction data by state and category.

3. `What technologies are used?`
[Python](https://www.python.org/) – Data extraction and processin
[Pandas](https://pandas.pydata.org/) – Data manipulation
[PostgreSQL](https://www.postgresql.org/) – Database storage
[SQL](https://en.wikipedia.org/wiki/SQL) – Data analysis
[Streamlit](https://docs.streamlit.io/) – Dashboard interface
[Plotly](https://plotly.com/) / [Matplotlib](https://matplotlib.org/) – Visualizations

4.`What insights are provided?`
-Total transactions and amounts by state, year, and quarter
-Popular transaction types (Recharge, P2P, Merchant Payments)
-State-wise insurance trends
-Device brand usage statistics
-User growth and app engagement

5.`How to run the project?`
```plaintext
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
streamlit run dashboard/app.py
```
6. `Can I contribute?`
Yes! Fork the repo, make your changes, and raise a pull request. All contributions are welcome.
**[`^        back to top        ^`](#Project-phonepe)**
















