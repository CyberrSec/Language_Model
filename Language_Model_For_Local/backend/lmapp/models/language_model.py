from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForSequenceClassification
import torch
from typing import Dict
import bleach

app = FastAPI(title="Advanced NLP API", description="API for text summarization and sentiment analysis")

class TextInput(BaseModel):
    text: str

class LanguageModelService:
    def __init__(self):
        # Load a more efficient summarization model
        self.summarizer_model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")
        self.summarizer_tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
        self.summarizer = pipeline("summarization", model=self.summarizer_model, tokenizer=self.summarizer_tokenizer)

        # Load sentiment analysis model
        self.sentiment_model = AutoModelForSequenceClassification.from_pretrained("roberta-large-mnli")
        self.sentiment_tokenizer = AutoTokenizer.from_pretrained("roberta-large-mnli")
        self.sentiment_analyzer = pipeline("zero-shot-classification", model=self.sentiment_model, tokenizer=self.sentiment_tokenizer)

    def summarize_text(self, text: str) -> str:
        # Sanitize input text
        text = bleach.clean(text)

        # Tokenize input text and check length
        input_tokens = self.summarizer_tokenizer.encode(text, return_tensors="pt")[0]
        input_length = len(input_tokens)

        # Define minimum length for meaningful summarization
        MIN_INPUT_LENGTH = 30
        MAX_TOKENS = 1024  # Model token limit
        CHUNK_SIZE = 512
        MAX_SUMMARY_LENGTH = 600

        if input_length < MIN_INPUT_LENGTH:
            return text

        # Set dynamic max_length and min_length based on input size
        max_length = min(int(input_length * 0.6), MAX_SUMMARY_LENGTH)
        min_length = max(5, int(input_length * 0.3))

        if input_length > MAX_TOKENS:
            # Handle long input text by chunking
            chunks = [text[i:i + CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]
            summaries = []
            for chunk in chunks:
                chunk_summary = self.summarizer(chunk, max_length=MAX_SUMMARY_LENGTH, min_length=min_length, truncation=True)[0]['summary_text']
                summaries.append(chunk_summary)
            final_summary = ' '.join(summaries)
            return final_summary[:input_length]

        # Directly summarize shorter inputs
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, truncation=True)[0]['summary_text']
        return summary

    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        # Sanitize input text
        text = bleach.clean(text)

        candidate_labels = ["Positive", "Negative", "Neutral"]
        results = self.sentiment_analyzer(text, candidate_labels, multi_label=False)
        
        sentiments = dict(zip(results['labels'], results['scores']))
        
        overall_sentiment = max(sentiments, key=sentiments.get)
        sentiments["overall"] = overall_sentiment
        
        return sentiments

language_model_service = LanguageModelService()

@app.post("/summarize", response_model=Dict[str, str])
async def summarize_text(input_data: TextInput):
    try:
        summary = language_model_service.summarize_text(input_data.text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/sentiment", response_model=Dict[str, float])
async def analyze_sentiment(input_data: TextInput):
    try:
        sentiment = language_model_service.analyze_sentiment(input_data.text)
        return sentiment
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
