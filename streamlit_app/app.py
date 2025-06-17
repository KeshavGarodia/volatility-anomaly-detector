import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.anomaly_detector import compute_features, detect_anomalies
from scripts.yahoo_scraper import fetch_yahoo_headlines as fetch_news
from scripts.llm_summarizer import summarize_anomaly

st.title("📉 Multi-Stock Volatility Anomaly Detector")

@st.cache_data
def load_data():
    df = pd.read_csv("data/all_stocks_5yr.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()
stock_names = df["Name"].unique()
selected = st.selectbox("Choose a stock", sorted(stock_names))

stock_df = df[df["Name"] == selected].copy()
stock_df = compute_features(stock_df)
stock_df = detect_anomalies(stock_df)

fig = px.line(stock_df, x="date", y="volatility", title=f"{selected} Volatility Over Time")
fig.add_scatter(x=stock_df[stock_df['is_anomaly']]["date"],
                y=stock_df[stock_df['is_anomaly']]["volatility"],
                mode='markers', marker=dict(color='red', size=8), name="Anomaly")

st.plotly_chart(fig, use_container_width=True)
st.subheader("🧠 Investigate Anomaly")

# Get list of anomaly dates
anomaly_dates = stock_df[stock_df['is_anomaly']]['date'].dt.strftime('%Y-%m-%d').tolist()

if not anomaly_dates:
    st.info("No anomalies detected for this stock.")
else:
    selected_date = st.selectbox("Select an anomaly date to investigate", anomaly_dates)
    if st.button("📎 Explain this spike"):
    	with st.spinner("Fetching news and generating explanation..."):
        	headlines = fetch_news(selected, selected_date)

        	if headlines and not all("No headlines found" in h for h in headlines):
            		summary = summarize_anomaly(selected, selected_date, headlines)
        	else:
            		summary = "No relevant news found to summarize."

        	st.markdown("**📰 Headlines:**")
        	if headlines:
            		for h in headlines:
                		st.markdown(f"- {h}")
        	else:
            		st.markdown("*No headlines available.*")

        	st.markdown("**🧠 LLM Summary:**")
        	st.success(summary)

