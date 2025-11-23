from transformers import pipeline

def load_model():
    """Load Hugging Face summarization model."""
    model = pipeline(
        "summarization",
        model="facebook/bart-large-cnn"
    )
    return model

def summarize_text(text, model, length_type):
    """Generate summary based on selected length."""
    
    if length_type == "Short":
        min_len, max_len = 30, 80
    elif length_type == "Medium":
        min_len, max_len = 60, 150
    else:  # Long
        min_len, max_len = 100, 250

    summary = model(
        text,
        min_length=min_len,
        max_length=max_len,
        do_sample=False
    )

    return summary[0]["summary_text"]
