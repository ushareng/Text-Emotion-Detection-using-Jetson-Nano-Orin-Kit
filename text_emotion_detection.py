import streamlit as st
from llama_cpp import Llama
import re

# Initialize the Llama model
llm = Llama(model_path="/home/usha/Desktop/work/llama.cpp/models/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf", n_ctx=512)

st.title("Text Emotion Detection")

input_text = st.text_area("Enter text to analyze:", "")

if st.button("Detect Emotion"):
    if input_text.strip():
        prompt = (
            "Determine the primary emotion of the following text. "
            "Respondthe emotion with exactly OE WORD only (joy, sadness, anger, fear, surprise, disgust, or neutral). "
            "No explanations.\n\n"
            f"Text: \"{input_text}\"\n\nEmotion:"
        )

        output = llm(prompt=prompt, max_tokens=50)  # Ensure short response

        response_text = output["choices"][0]["text"].strip()
        print("output is ", response_text)

        # Extract only the first valid word (remove extra symbols or multiple words)
        #  match = re.search(r"\b(joy|sadness|anger|fear|surprise|disgust|neutral)\b", response_text, re.IGNORECASE)
        # detected_emotion = match.group(0).lower() if match else "neutral"
        detected_emotion = response_text.split()[0] if response_text else "neutral"

        st.success(f"Detected Emotion: {detected_emotion}")
    else:
        st.error("Please enter some text to analyze.")

