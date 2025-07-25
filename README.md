# Project phonepe

**PhonePe Pulse**  Transaction Insights – Data Analysis & Visualization Project

## Overview
This project leverages the PhonePe Pulse Dataset to explore, analyze, and visualize digital transaction trends across India. The insights are drawn from various dimensions such as state-wise transaction patterns, device usage behavior, insurance penetration, and user engagement over time.

The goal of this project is to extract meaningful business insights that can support decision-making for marketing, expansion, and user engagement strategies.

The Indian digital payments story has truly captured the world’s imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by mobile phone penetration, internet access, and state-of-the-art payments infrastructure.

PhonePe, launched in 2016, has played a significant role in this transformation. As a way to give back to the data and developer community, PhonePe released the PhonePe Pulse Dataset API, which is licensed under [LICENSE](LICENSE) — an open data initiative to demystify digital payments in India.

## Table of Contents
PhonePe Pulse - Data
Announcements
Table of Contents
Goal
Guide
Documentation
Folder Structure
JSON Structure / Syntax
Aggregated
data/aggregated/transaction/country/india/2018/1.json
data/aggregated/user/country/india/2021/1.json
data/aggregated/insurance/country/india/2021/1.json
Map
data/map/transaction/hover/country/india/2021/1.json
data/map/user/hover/country/india/2021/1.json
data/map/insurance/hover/country/india/2021/1.json
Top
data/top/transaction/country/india/2021/1.json
data/top/user/country/india/2021/1.json
data/top/insurance/country/india/2021/1.json
FAQs
LICENSE

## Goal
The goal of this project is to analyze and visualize the PhonePe Pulse dataset to uncover insights into digital payment trends across India.

## Guide
This data has been structured to provide details of following three sections with data cuts on Transactions, Users and Insurance of PhonePe Pulse - Explore tab.

1.Aggregated - Aggregated values of various payment categories as shown under Categories section
2.Map - Total values at the State and District levels.
3.Top - Totals of top States / Districts /Pin Codes
All the data provided in these folders is of JSON format. For more details on the structure/syntax you can refer to the JSON Structure / Syntax section of the documentation.


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
