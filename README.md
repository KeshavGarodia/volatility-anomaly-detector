📉 Volatility Anomaly Detector
An interactive Streamlit app that detects unusual spikes or drops in stock volatility across multiple assets and explains them using recent news and an LLM-based summarizer.

🚀 Features
📊 Detects volatility anomalies in historical stock data

📈 Computes returns, volume, and rolling volatility features

🔍 Scrapes recent news headlines from Yahoo Finance

🧠 Generates concise explanations using a local LLM (Flan-T5)

🌐 Fully interactive dashboard built with Streamlit

🛠️ Tech Stack
Python (pandas, numpy, scikit-learn, requests)

Streamlit for the frontend UI

BeautifulSoup for news scraping

Transformers for local LLM summarization (Flan-T5)

Matplotlib for plotting

Git + GitHub for version control

🗂️ Project Structure
volatility-anomaly-detector/
├── data/ # CSV files with stock data
├── scripts/ # Core logic: anomaly detection, scraping, summarization
├── streamlit_app/ # Streamlit frontend
├── test_scraper.py # For testing Yahoo news scraping
└── README.md

📦 Setup Instructions
Clone the repo:
git clone https://github.com/KeshavGarodia/volatility-anomaly-detector.git
cd volatility-anomaly-detector

Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run streamlit_app/app.py

✨ Example Output
Anomaly detected on 2021-01-27 for TSLA

Headlines scraped from Yahoo Finance

Local LLM generates: “Tesla stock surged following better-than-expected Q4 results.”

🧠 Motivation
This project bridges finance and AI — giving insights into market anomalies using real data and intelligent summarization, even with no OpenAI API costs.

