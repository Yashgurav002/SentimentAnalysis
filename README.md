# 🎭 Sentiment Analysis + Emotion Classifier

A dual NLP pipeline app built with **HuggingFace Transformers** and deployed as a live interactive demo on **HuggingFace Spaces** using Gradio.

[![Live Demo](https://img.shields.io/badge/🤗%20HuggingFace-Live%20Demo-yellow)](https://huggingface.co/spaces/Yash-2002/SentimentAnalysisBasic)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-orange)](https://huggingface.co/docs/transformers)
[![Gradio](https://img.shields.io/badge/Gradio-UI-green)](https://gradio.app/)

---

## 🔗 Live Demo

👉 **[Try it here → huggingface.co/spaces/Yash-2002/SentimentAnalysisBasic](https://huggingface.co/spaces/Yash-2002/SentimentAnalysisBasic)**

---

## 📌 What It Does

Given any input text, the app runs **two separate NLP pipelines** and returns:

| Pipeline | Model | Output |
|---|---|---|
| **Sentiment Analysis** | `distilbert-base-uncased-finetuned-sst-2-english` | POSITIVE / NEGATIVE + confidence score |
| **Emotion Classification** | `SamLowe/roberta-base-go_emotions` | Top 2 emotions (e.g. admiration, joy, annoyance) + scores |

### Example Output
```
Input: "I love building AI projects but debugging is frustrating!"

Sentiment: POSITIVE (87.4%)

Emotions:
- admiration: 61.2%
- annoyance: 24.3%
```

---

## 🛠️ Tech Stack

- **[HuggingFace Transformers](https://huggingface.co/docs/transformers)** — pre-trained NLP pipeline abstraction
- **[Gradio](https://gradio.app/)** — interactive web UI
- **[distilBERT](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)** — lightweight BERT variant fine-tuned on SST-2 for sentiment
- **[RoBERTa / GoEmotions](https://huggingface.co/SamLowe/roberta-base-go_emotions)** — multi-label emotion classification across 27 categories
- **HuggingFace Spaces** — free cloud deployment with Docker

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/Yashgurav002/SentimentAnalysis.git
cd SentimentAnalysis
```

**2. Install dependencies**
```bash
pip install transformers torch gradio
```

**3. Run the app**
```bash
python app.py
```

Open `http://localhost:7860` in your browser.

---

## 📁 Project Structure

```
SentimentAnalysis/
├── app.py              # Main Gradio app with both pipelines
├── requirements.txt    # Dependencies for HuggingFace Spaces
└── README.md
```

---

## 💡 Key Concepts Demonstrated

- Using HuggingFace `pipeline()` abstraction for zero-boilerplate inference
- Running **multiple models** in a single app
- Wrapping transformer models in a **Gradio UI**
- Deploying ML apps to **HuggingFace Spaces** (free cloud hosting)
- Managing **two Git remotes** (HuggingFace + GitHub)

---

## 🧠 Models Used

### 1. `distilbert-base-uncased-finetuned-sst-2-english`
- Distilled version of BERT — 40% smaller, 60% faster
- Fine-tuned on Stanford Sentiment Treebank (SST-2)
- Binary classification: POSITIVE / NEGATIVE

### 2. `SamLowe/roberta-base-go_emotions`
- Based on RoBERTa architecture
- Trained on Google's GoEmotions dataset (58k Reddit comments)
- Classifies across 27 emotion categories

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 👤 Author

**Yash Gurav**
- 🤗 HuggingFace: [Yash-2002](https://huggingface.co/Yash-2002)
- 💼 B.E. in AI & Data Science | Oracle Certified (GenAI, AI Foundations, Cloud Foundations)
- 🔗 [GitHub](https://github.com/Yashgurav002)