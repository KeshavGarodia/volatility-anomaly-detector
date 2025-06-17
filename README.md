# 📉 Volatility Anomaly Detector

An interactive Streamlit app that detects unusual spikes or drops in stock volatility across multiple assets and explains them using recent news and a local LLM summarizer.

---

## 🚀 Features

- 📊 Detects volatility anomalies in historical stock data  
- 📈 Computes returns, volume, and rolling volatility features  
- 🔍 Scrapes recent news headlines from Yahoo Finance  
- 🧠 Summarizes headlines using a local LLM (Flan-T5)  
- 🌐 Interactive dashboard built with Streamlit  

---

## 🛠️ Tech Stack

- **Python** (pandas, numpy, scikit-learn)  
- **Streamlit** for UI  
- **BeautifulSoup** for web scraping  
- **Transformers** from Hugging Face for LLM summarization  
- **Matplotlib** for plotting  
- **Git + GitHub** for version control  

---

## 🗂️ Project Structure

```
volatility-anomaly-detector/
├── data/                  # Stock data CSVs
├── scripts/               # Core logic modules
│   ├── anomaly_detector.py
│   ├── yahoo_scraper.py
│   └── llm_summarizer.py
├── streamlit_app/         # Streamlit frontend
│   └── app.py
├── test_scraper.py        # Debug script for scraping
└── README.md
```

---

## 📦 Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/KeshavGarodia/volatility-anomaly-detector.git
   cd volatility-anomaly-detector
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run streamlit_app/app.py
   ```

---

## ✨ Example Output

- **Anomaly Detected**: TSLA on 2022-01-27  
- **Headlines**: Scraped from Yahoo Finance  
- **LLM Summary**: "Tesla stock surged after strong Q4 results beat expectations."

---

## 🧠 Motivation

This project blends AI and financial analytics to explain unusual volatility patterns using real-world news — all without needing OpenAI API access. Powered by local models, it’s fast, free, and insightful.

---

## 📜 License

MIT License
