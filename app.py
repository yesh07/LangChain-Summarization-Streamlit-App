# Importing the dependency
import streamlit as st

# Copy in OpenAI
from langchain.llms import OpenAI

# Prompt Template
from langchain.prompts import PromptTemplate

# LLM Chain
from langchain.chains import LLMChain

# Bringing in the API Key
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'

# Build up a chain
llm = OpenAI(temperature=0)

template = PromptTemplate(input_variables=['summary_block'], template= '''Summarise the following block of text:{summary_block}''')

chain = LLMChain(llm=llm, prompt=template)

# Writing Streamlit to the screen
st.title('🚀 Summarization Streamlit App')

# Prompt bar is here
prompt = st.chat_input('Pass through a summarization prompt here')

# Trigger if user hits enter
if prompt:
    # Rendering the user outputto the screen
    st.chat_message('human', avatar='👨‍💻').markdown(prompt)

    # Get the response from the LLM
    response = chain.run(prompt)

    # Display LLM output back to the screen
    st.chat_message('ai', avatar='🤖').markdown(response)