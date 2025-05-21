import streamlit as st
from transformers import pipeline

# Initialize the model
model_name = "microsoft/phi-2"  # or "gpt2-medium"
generator = pipeline("text-generation", model=model_name, device=-1)  # Use CPU for now; we'll switch to GPU in Colab for testing

def build_prompt(topic):
    return f"""
Explain the following topic to a 10-year-old in 2 short sentences. Use simple words and include a real-world example.

Topic: Machine learning
A: It's when computers learn from examples to do tasks like guessing what's in a picture.

Topic: Photosynthesis
A: It's how plants make food from sunlight, like when a leaf turns sunshine into sugar.

Topic: Python
A: It's a programming language people use to tell computers what to do, like making games or apps.

Topic: {topic}
A:"""  # No space or newline after the colon

def is_valid_response(text, topic):
    text_lower = text.lower()
    if topic.lower() == "photosynthesis":
        return (
            any(word in text_lower for word in ["plant", "sun", "light"]) 
            and any(word in text_lower for word in ["food", "sugar", "energy"])
        )
    if topic.lower() == "python":
        return any(word in text_lower for word in ["programming", "code", "language"])
    if topic.lower() == "machine learning":
        return (
            any(word in text_lower for word in ["computers", "machines", "systems"]) 
            and "learn" in text_lower
        )
    return len(text.split()) > 8

def get_fallback_response(topic):
    if topic.lower() == "machine learning":
        return "It's when computers learn from examples to do tasks like guessing what's in a picture."
    if topic.lower() == "photosynthesis":
        return "It's how plants make food from sunlight, like when a leaf turns sunshine into sugar."
    if topic.lower() == "python":
        return "It's a programming language people use to tell computers what to do, like making games or apps."
    return "Explanation unavailable."

# Streamlit app interface
st.title("Kid-Friendly Topic Explainer")
st.write("Enter a topic, and I'll explain it in simple terms for a 10-year-old!")

# Input field for the topic
topic = st.text_input("Topic:", value="Photosynthesis")

# Button to generate explanation
if st.button("Generate Explanation"):
    prompt = build_prompt(topic)
    try:
        # Generate output
        output = generator(prompt, max_new_tokens=60, temperature=0.7, do_sample=True)
        generated = output[0]["generated_text"]

        # Extract the answer after "A:"
        answer_section = generated.split(f"Topic: {topic}\nA:")[-1].strip()
        answer = answer_section.split("\n")[0].split("Topic:")[0].strip()

        # Validate the response
        if is_valid_response(answer, topic):
            st.success("Explanation:")
            st.write(answer)
        else:
            st.warning("Fallback Explanation:")
            st.write(get_fallback_response(topic))

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.write("Please try a different topic or check the model setup.")
