from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain.prompts import PromptTemplate
import json
import os

load_dotenv()

def load_prompt(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error(f"Template file '{file_path}' not found!")
        return None

# Initialize the model
model = ChatOpenAI()

st.header("research tool")
paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]) 

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

# Create the prompt template
prompt_template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:  
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:  
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
    input_variables=['paper_input', 'style_input', 'length_input']
)

if st.button("generate"):
    # Format the prompt with user inputs
    formatted_prompt = prompt_template.format(
        paper_input=paper_input,
        style_input=style_input,
        length_input=length_input
    )
    
    # Send the formatted prompt to the model
    result = model.invoke(formatted_prompt)
    st.write(result.content)  # Access the content of the response
