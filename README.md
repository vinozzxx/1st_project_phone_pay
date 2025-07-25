# 📱 1st_project_phone_pay

A data analysis and visualization project using **PhonePe Pulse** data.

## 📌 Project Overview

This project focuses on analyzing digital transaction trends across India using the PhonePe Pulse dataset. It includes:

- Data extraction from PhonePe Pulse
- Data cleaning and transformation using Python
- Storage in PostgreSQL database
- Analytical queries using SQL
- Interactive visualizations using Python and Streamlit

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

![PhonePe Dashboard
](http://localhost:8503/)

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
