import streamlit as st
import google.generativeai as geneai
from dotenv import load_dotenv
import os

# load the env
load_dotenv()

# get the api key
api_key = os.getenv('GOOGLE_API_KEY')

# define the model
model = geneai.GenerativeModel("gemini-pro")

# set page title
st.set_page_config()
st.title("Ask Me Anythings...!")

# user input
text_input = st.text_input(label= "Enter Your Prompts here")
submit_button = st.button(label='Submit')

if submit_button:    
    response = model.generate_content(text_input)
    st.write(response.text)
