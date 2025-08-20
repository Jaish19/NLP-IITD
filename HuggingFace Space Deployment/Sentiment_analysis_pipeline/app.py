import gradio as gr
from transformers import pipeline

pipe = pipeline("sentiment-analysis")
# pipe = pipeline("text-classification", model="ProsusAI/finbert")

def analyze(text):
    if text:
        return pipe(text)
    return {"message": "Please enter some text"}

demo = gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Enter your input:", lines=5, placeholder="Type something..."),
    outputs=gr.JSON(label="Output"),
    title="Sentiment Analysis",
    description="Enter text below to analyze sentiment using Hugging Face Transformers."
)

if __name__ == "__main__":
    demo.launch()
