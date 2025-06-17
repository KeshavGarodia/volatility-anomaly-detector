from transformers import pipeline

# Load local summarization pipeline
summarizer = pipeline("text2text-generation", model="google/flan-t5-base")

def summarize_anomaly(stock_name: str, date: str, headlines: list[str]) -> str:
    if not headlines or all("No headlines found" in h for h in headlines):
        return f"No news headlines were found for {stock_name} on {date}."

    prompt = (
        f"The following are news headlines for {stock_name} on {date}:\n\n"
        + "\n".join(f"- {h}" for h in headlines[:8])
        + "\n\nBased on this, summarize in one sentence what might have caused a significant price spike or drop."
    )

    result = summarizer(
        prompt,
        max_new_tokens=64,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]
