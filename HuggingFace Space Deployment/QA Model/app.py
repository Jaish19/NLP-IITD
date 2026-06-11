import os
import gradio as gr
from huggingface_hub import InferenceClient

# Read HF token from Space Secrets
HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="auto",
    api_key=HF_TOKEN,
)

def answer_question(context, question):
    try:
        result = client.question_answering(
            question=question,
            context=context,
            model="distilbert/distilbert-base-uncased-distilled-squad",
        )

        return f"""
Answer: {result.answer}

Score: {result.score:.4f}

Start Position: {result.start}

End Position: {result.end}
"""
    except Exception as e:
        return f"Error: {str(e)}"


demo = gr.Interface(
    fn=answer_question,
    inputs=[
        gr.Textbox(
            label="Context",
            lines=6,
            placeholder="Enter the context here..."
        ),
        gr.Textbox(
            label="Question",
            placeholder="Ask a question..."
        )
    ],
    outputs=gr.Textbox(label="Result", lines=8),
    title="Question Answering Demo",
    description="Ask questions from the given context using DistilBERT SQuAD model.",
)

if __name__ == "__main__":
    demo.launch()
