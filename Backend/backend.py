from fastapi import FastAPI
from pydantic import BaseModel
from checking import lang_map
import model

app = FastAPI()

class TranslateRequest(BaseModel):
    src: str
    tgt: str
    text: str

@app.post("/translate")
def translate(req: TranslateRequest):
    try:
        # Convert human-readable names to HF codes
        src_code = lang_map.get(req.src)
        tgt_code = lang_map.get(req.tgt)

        print("Body:", req.dict())
        print("Source code:", src_code)
        print("Target code:", tgt_code)

        if not src_code or not tgt_code:
            return {"error": f"Invalid src/tgt: {req.src}, {req.tgt}"}

        # dummy translation
        translated = f"[{src_code} → {tgt_code}] {req.text}"
        # Call your Hugging Face model
        trans=model.translate(req.text, src_code, tgt_code)

        return {"translation": trans}

    except Exception as e:
        import traceback
        traceback.print_exc()   # log the full error
        return {"error": str(e)}   # return the real error message

#This is where you can verify backend : http://127.0.0.1:8889/docs#/default/translate_translate_post