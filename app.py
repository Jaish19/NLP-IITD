import gradio as gr
from transformers import pipeline

# Load Hugging Face pipeline
pipe = pipeline(
    "text-classification",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Prediction function
def predict_sentiment(text):
    if not text.strip():
        return "Please enter some text."

    result = pipe(text)[0]

    label = result["label"]
    score = round(result["score"] * 100, 2)

    return f"Sentiment: {label}\nConfidence: {score}%"

# Gradio UI
demo = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(
        lines=4,
        placeholder="Enter your review or sentence here..."
    ),
    outputs=gr.Textbox(label="Prediction"),
    title="Sentiment Analysis App",
    description="This app uses DistilBERT fine-tuned on SST-2 for sentiment classification."
)

# Launch app
demo.launch()
