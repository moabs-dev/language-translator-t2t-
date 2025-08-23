import os
import requests
from dotenv import load_dotenv
# Load .env file
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY")
# Pick a translation model
MODEL_ID = "facebook/mbart-large-50-many-to-many-mmt"
# API endpoint
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"
headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}
# Example: English -> Urdu
def translate(text, src, tgt):
    payload = {
        "inputs": text,
        "parameters": {"src_lang": src, "tgt_lang":tgt } #Add : "forced_bos_token_id": tgt in parameters ,it helps sometimes 
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["translation_text"]
#print(translate("Moeen is a good boy.", "en_XX", "ur_PK"))


#This could also work :

# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()
# HF_TOKEN = os.getenv("HUGGINGFACE_API_KEY").strip()

# API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
# headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# # Example text to translate
# payload = {
#     "inputs": "Hello, how are you?",
#     "parameters": {"src_lang": "en_XX", "tgt_lang": "fr_XX"}
# }

# response = requests.post(API_URL, headers=headers, json=payload)
# print("Status code:", response.status_code)
# print("Response text:", response.text)

# if response.status_code == 200:
#     data = response.json()  # Now it should succeed
#     print(data)
# else:
#     print("Error:", response.text)
