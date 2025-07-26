# Project phonepe

**PhonePe Pulse**  Transaction Insights – Data Analysis & Visualization Project

## Overview
This project leverages the PhonePe Pulse Dataset to explore, analyze, and visualize digital transaction trends across India. The insights are drawn from various dimensions such as state-wise transaction patterns, device usage behavior, insurance penetration, and user engagement over time.

The goal of this project is to extract meaningful business insights that can support decision-making for marketing, expansion, and user engagement strategies.

The Indian digital payments story has truly captured the world’s imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by mobile phone penetration, internet access, and state-of-the-art payments infrastructure.

PhonePe, launched in 2016, has played a significant role in this transformation. As a way to give back to the data and developer community, PhonePe released the PhonePe Pulse Dataset API, which is licensed under [LICENSE](LICENSE) — an open data initiative to demystify digital payments in India.

## Table of Contents
- [PhonePe Pulse - Data](#phonepe-pulse---data)
- [Overview](#Overview)
- [Table of Contents](#table-of-contents)
- [Goal](#goal)
- [Guide](#guide)

---

## Goal
The goal of this project is to analyze and visualize the PhonePe Pulse dataset to uncover insights into digital payment trends across India.

## Guide

Follow these steps to explore the dataset:

1. Clone the repository
2. Navigate to the data folder
3. Use Python scripts to extract insights

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

#### Structure Breakdown:

- The data is organized at two levels: **Country** and **State**.
- Inside the `country/india` folder, data is grouped by **year** (e.g., 2018, 2019, etc.).
- Similarly, the `state` folder contains subfolders for each **state** in India, also grouped by **year**.

#### File Naming:

- Each year folder (both for country and state) includes **up to four JSON files**:
  - `1.json`, `2.json`, `3.json`, `4.json`
  - These represent **Quarter 1 to Quarter 4** of that year.

---

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
...
## Data Extraction – Aggregated Insurance (State-Level)
The following Python code extracts aggregated insurance data at the state level from the PhonePe Pulse dataset. It navigates through nested directories and reads JSON files representing different years and quarters.

# How it works:
Navigates through this folder path:

data/aggregated/insurance/country/india/state/{state}/{year}/{quarter}.json

Extracts:
-State
-Year
-Quarter
-Transaction Type
-Transaction Count
-Transaction Amount

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
...
## JSON Structure (Sample)
```plaintext
Sample file path:
data/aggregated/insurance/country/india/state/delhi/2018/1.json
Sample JSON:
json
Copy code
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

## 📌 Project Overview

This project focuses on analyzing digital transaction trends across India using the PhonePe Pulse dataset. It includes:

- Analyze transaction behavior across states, quarters, and payment categories.
- Understand user engagement across device brands and app usage.
- Explore insurance transaction growth and regional adoption.
- Build a dashboard for interactive data visualization and business insights.

## 🧰 Tech Stack

- **Python** – Data analysis and visualization
- **PostgreSQL** – Data storage and querying
- **Pandas, Plotly, Matplotlib** – Data manipulation and plotting
- **Streamlit** – Dashboard development
- **GeoJSON** – Mapping state boundaries for choropleth maps

## 🔍 Key Features

- 📊 Bar, line, and pie charts of transaction data
- 🗺️ Choropleth map showing state-wise transaction values
- 📅 Filters for Year and Quarter selection
- 🏆 Top-performing states displayed dynamically
- 🧠 Business insights and KPIs visualized

## 📷 Dashboard Preview

![PhonePe Dashboard ScreenShort]("C:\Users\Admin\OneDrive\Videos\Pictures\Screenshots\Screenshot (26).png")

## 📁 Project Structure

```bash
📁 1st_project_phone_pay/
│
├── 📂 data/                     # Processed data or raw GeoJSON files
├── 📂 scripts/                  # Python scripts for ETL and analysis
├── 📂 streamlit_app/            # Streamlit dashboard files
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # Project overview
└── 📄 phonepe_dashboard.py      # Main Streamlit dashboard file
