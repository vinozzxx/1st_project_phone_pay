# 📱 1st_project_phone_pay

A data analysis and visualization project using **PhonePe Pulse** data.
PhonePe Pulse Transaction Insights – Data Analysis & Visualization Project
🔍 Overview
This project leverages the PhonePe Pulse Dataset to explore, analyze, and visualize digital transaction trends across India. The insights are drawn from various dimensions such as state-wise transaction patterns, device usage behavior, insurance penetration, and user engagement over time.

The goal of this project is to extract meaningful business insights that can support decision-making for marketing, expansion, and user engagement strategies.

The Indian digital payments story has truly captured the world’s imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by mobile phone penetration, internet access, and state-of-the-art payments infrastructure.

PhonePe, launched in 2016, has played a significant role in this transformation. As a way to give back to the data and developer community, PhonePe released the PhonePe Pulse Dataset API, which is licensed under CDLA-Permissive-2.0 — an open data initiative to demystify digital payments in India.


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
