# Azure Telemetry Lakehouse

## Overview
This project demonstrates an end-to-end data engineering workflow for telemetry-style sensor data using an Azure-inspired Lakehouse architecture.

The solution is designed around a predictive maintenance use case using aircraft engine degradation data. It includes ingestion, transformation, data quality checks, and preparation of ML-ready datasets for downstream analytics and modeling.

## Business Context
Telemetry data from industrial and aviation systems is often high-volume, noisy, and difficult to use directly for analytics. To support reliable reporting and machine learning, raw sensor data must be ingested, validated, standardized, and transformed into curated datasets.

This project simulates that workflow using layered data engineering principles.

## Architecture
- Raw data ingestion into Bronze layer
- Transformation and validation into Silver layer
- Curated analytical dataset in Gold layer
- ML-ready dataset for predictive maintenance use cases

## Tech Stack
- Python
- Pandas
- Azure Data Factory
- Azure Data Lake Storage
- Azure SQL Database
- GitHub

## Project Structure
```text
azure-telemetry-lakehouse/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── ingestion/
│   ├── transformation/
│   ├── quality/
│   └── utils/
├── docs/
├── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
