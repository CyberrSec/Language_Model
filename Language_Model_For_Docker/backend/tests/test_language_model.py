# test_language_model.py

from lmapp.models.language_model import LanguageModelService

def test_summarize_short_text():
    service = LanguageModelService()
    result = service.summarize_text("Short text.")
    assert result == "Short text."

def test_summarize_long_text():
    service = LanguageModelService()
    long_text = "This is a long text that should be summarized. " * 20
    result = service.summarize_text(long_text)
    assert len(result) < len(long_text)
    assert isinstance(result, str)

def test_analyze_sentiment_positive():
    service = LanguageModelService()
    result = service.analyze_sentiment("I am very happy today!")
    assert "Positive" in result
    assert result["overall"] == "Positive"

def test_analyze_sentiment_negative():
    service = LanguageModelService()
    result = service.analyze_sentiment("I am very sad today.")
    assert "Negative" in result
    assert result["overall"] == "Negative"

def test_analyze_sentiment_neutral():
    service = LanguageModelService()
    result = service.analyze_sentiment("This is a statement.")
    assert "Neutral" in result
    assert result["overall"] == "Neutral"
