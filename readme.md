# 🌐 Language Translator (T2T)

A robust translation platform leveraging Hugging Face's mBART model to facilitate seamless multilingual communication. This project encompasses both frontend and backend components, each encapsulated within Docker containers for streamlined deployment and scalability.

---

## Overview
language-translator-t2t- is an open-source developer tool designed to facilitate comprehensive multilingual translation workflows across speech and text. It integrates state-of-the-art models, RESTful APIs, and intuitive interfaces to enable seamless language conversions in diverse applications.

Why language-translator-t2t-?
This project simplifies complex multilingual processing by providing:

Modular Architecture: Combines backend models, API endpoints, and frontend interfaces for a cohesive experience.

Containerized Deployment: Uses Docker to ensure consistent environments across development and production.

Multilingual Support: Leverages Hugging Face models and language mapping for accurate translations.

User-Friendly Interface: Streamlit-based frontend for easy language selection and translation visualization.
Seamless Integration: FastAPI backend connects models with client applications efficiently.

Comprehensive Guidance: Clear documentation for executing all core translation tasks- speech-to-speech, speech-to-text, text-to-speech, and text-to-text.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)

### Clone the Repository

```bash
git clone https://github.com/moabs-dev/language-translator-t2t-.git
cd language-translator-t2t-
```

### Build and Run the Containers

You can run the project locally using Docker Compose:

```bash
docker-compose build
docker-compose up -d
```

This will build the frontend and backend images and start the containers. No need to manually tag or push to Docker Hub unless you want to share your images.

### Pull Prebuilt Docker Images

If you prefer to use prebuilt images, you can pull them directly from Docker Hub:

```bash
# Backend
docker pull moinboss/translator-backend:latest

# Frontend
docker pull moinboss/translator-frontend:latest
```

Then simply run:

```bash
docker-compose up -d
```

---

## 🧠 Backend (Translator API)

The backend is powered by Hugging Face's mBART model, enabling translations between multiple languages.

### Setup

1. Create a `.env` file in the root directory with the following content:

   ```
   HUGGINGFACE_API_KEY=your_huggingface_api_key
   ```

2. Build and run the backend container:

   ```bash
   docker-compose up --build backend
   ```

### API Endpoint

- **URL:** `http://localhost:5000/translate`
- **Method:** `POST`
- **Payload:**

  ```json
  {
    "text": "Hello, world!",
    "src_lang": "en_XX",
    "tgt_lang": "fr_XX"
  }
  ```

- **Response:**

  ```json
  {
    "translation_text": "Bonjour, le monde!"
  }
  ```

### Challenges Faced

- Calling the Hugging Face API directly was more challenging than importing and using the transformer library locally.
- Handling authentication, headers, and JSON payloads required careful attention.
- Debugging API responses and ensuring correct language codes took more effort than expected.

Despite these challenges, we successfully integrated the API to work seamlessly with our backend.

---

## 🎨 Frontend (Translator UI)

The frontend provides an intuitive interface for users to input text and receive translations.

### Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

The application will be available at `http://localhost:3000`.

---

## 🧪 Testing

To run tests for both frontend and backend:

```bash
docker-compose run --rm backend pytest
docker-compose run --rm frontend npm test
```

---

## 🛠️ Docker Commands

### Build Images

```bash
docker build -t moinboss/translator-backend:latest -f backend/Dockerfile .
docker build -t moinboss/translator-frontend:latest -f frontend/Dockerfile .
```

### Run Containers

```bash
docker run -p 5000:5000 moinboss/translator-backend:latest
docker run -p 3000:3000 moinboss/translator-frontend:latest
```

> Note: Manually tagging and pushing to Docker Hub is optional; using `docker-compose build` and `docker-compose up -d` is sufficient for running the project locally.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

