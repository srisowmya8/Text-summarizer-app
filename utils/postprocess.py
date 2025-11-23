import re

def clean_summary(summary):
    """Remove repeated spaces, sentences, or artifacts."""
    summary = summary.strip()
    summary = re.sub(r'\s+', ' ', summary)
    summary = summary.replace(" .", ".")
    return summary
