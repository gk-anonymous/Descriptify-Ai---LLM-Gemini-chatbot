from dotenv import load_dotenv
load_dotenv()
from PIL import Image

import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_reponse(input,image):
    if input!=" ":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

#initilize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("LLM Application")

input = st.text_input("input Prompt:",key="input")

uploaded_file = st.file_uploader("Choose an image..", type=["jpg","jpeg","png","jfif"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.",use_column_width=True)


submit = st.button("Tell me about the Image")

##if submit is clicked
if submit:
    response = get_gemini_reponse(input,image)
    st.subheader("The Response is")
    st.write(response)
