import streamlit as st
from utils.preprocess import clean_text, split_text
from utils.summarizer import load_model, summarize_text
from utils.postprocess import clean_summary

# Load model once (cached for speed)
model = load_model()

st.title("📝 AI Text Summarizer App")
st.write("Paste any long text below and get a clean summary instantly.")

# User Input
text = st.text_area("Enter text to summarize", height=250)

summary_length = st.selectbox(
    "Choose summary length:",
    ["Short", "Medium", "Long"]
)

if st.button("Summarize"):
    if not text.strip():
        st.error("Please enter some text first.")
    else:
        with st.spinner("Summarizing..."):
            cleaned = clean_text(text)
            chunks = split_text(cleaned)

            summaries = []

            for chunk in chunks:
                result = summarize_text(chunk, model, summary_length)
                cleaned_result = clean_summary(result)
                summaries.append(cleaned_result)

            final_output = " ".join(summaries)
            final_output = clean_summary(final_output)

        st.subheader("Summary:")
        st.write(final_output)

        st.download_button(
            "Download Summary",
            final_output,
            file_name="summary.txt"
        )
