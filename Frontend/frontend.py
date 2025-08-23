import streamlit as st
import requests
from checking import bef
from checking import lang_map

st.set_page_config(page_title='Multilanguage translator UI', layout='centered')

#API_URL = 'http://127.0.0.1:8889/translate' 
API_URL = 'http://backend:8889/translate'  #Using this when using docker, otherwise above line is good to go
st.title("🌐 Language Translator")

# Dropdowns
source = st.selectbox("Source Language", bef)
text = st.text_area('Input text here:', height=70, placeholder='My name is Moeen.')
target = st.selectbox("Target Language", bef)

if st.button("Translate"):
    if text.strip():
        # Convert to HuggingFace language codes before sending
        # src_code = lang_map[source]  #this  thing already done is backend so no need here
        # tgt_code = lang_map[target]

        if not source or not target:
            st.error("❌ Unsupported language selection")
        else:
            payload = {
                "src": source,   # send codes, not names
                "tgt": target,
                "text": text
            }
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                response_data = response.json()
                #st.write("DEBUG:", response_data)
                if 'error' in response_data:
                    st.error(response_data['error'])
                else:
                    translated = response_data['translation']
                    st.subheader('Translated text:')
                    st.markdown(f'**Here:** {translated}')
            else:
                st.error(f"⚠️ API Error: {response.status_code}")
    else:
        st.warning("⚠️ Please enter some text to translate.")
