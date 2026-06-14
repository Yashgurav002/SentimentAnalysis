import gradio as gr
from transformers import pipeline

# Sentiment Analysis
sentiment_pipe = pipeline("sentiment-analysis")  # uses distilbert by default

# Text Classification (emotion detection - more interesting!)
classifier = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    top_k=2
)

def analyze(text):
    sentiment = sentiment_pipe(text)[0]
    emotions = classifier(text)[0]

    result = f"**Sentiment:** {sentiment['label']} ({sentiment['score']:.2%})\n\n"
    result += "**Emotions:**\n"
    for e in emotions:
        result += f"- {e['label']}: {e['score']:.2%}\n"
    return result

demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Enter text", placeholder="Type something..."),
    outputs=gr.Markdown(label="Analysis"),
    title="🎭 Sentiment + Emotion Classifier",
    description="Dual analysis using HuggingFace pipelines"
)

demo.launch()

