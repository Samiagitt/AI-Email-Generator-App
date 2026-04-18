import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

dotenv=load_dotenv()

api_key=os.getenv("OPENAI_API_KEY")

client=OpenAI(api_key=api_key)

if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

st.title("Email Generator")
st.subheader("Enter the details how you want to generate the email")

Instruction=st.text_area("please enter your preferred email type", height=200)
email_type=st.selectbox("choose your preferred language",
             ["English","Bengali","Hindi","Arabic","Chinese","Japanese","Spanish"]
             )
if st.button("Generate email:"):
    if email_type=="English":
        response="""Generate an email in english language with following details:"""
    elif email_type=="Bengali":
        response="""Generate an email in bengali language with following details:"""
    elif email_type=="Hindi":
        response="""Generate an email in hindi language with following details:"""
    elif email_type=="Arabic":
        response="""Generate an email in arabic language with following details:"""
    elif email_type=="Chinese":
        response="""Generate an email in chinese language with following details:"""
    elif email_type=="Japanese":
        response="""Generate an email in japanese language with following details:"""
    else:
        response="""Generate an email in japanese language with following details:"""
        
    prompt=f"""{response}
    Generate an email in {email_type}language with following details:
    {Instruction}
    """
     
    with st.spinner("Generating email..."):
        result= client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
    st.subheader("Generated email:")
    st.write(result.output_text)