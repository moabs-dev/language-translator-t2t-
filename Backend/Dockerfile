FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8889"] 
#Streamlit host at 0.0.0.0 or simply localhost and we have set port in frontend and backend codes
