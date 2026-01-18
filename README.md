# Transly – Translation Application Backend

**Smart India Hackathon 2025**

Backend system for **Transly**, a multilingual translation application supporting **Text Translation, OCR, Speech-to-Text Translation, and Chatbot interactions**, with secure per-user data storage.

---

## 📌 Project Overview

The Transly backend is designed to handle **user authentication** and **history management** for all translation-related modules.
It ensures **secure access**, **scalable data storage**, and **smooth integration** with AI models and frontend clients.

---

## 🧩 Core Modules & Data Storage

| Module                  | Description                                  |
| ----------------------- | -------------------------------------------- |
| **User Authentication** | User signup, login, JWT-based authentication |
| **Translation History** | Text input and translated output             |
| **OCR History**         | Image → extracted text → translated text     |
| **Speech History**      | Audio → transcribed text → translated output |
| **Chatbot History**     | User messages and chatbot responses          |

✔ All data stored **per user**
✔ Secure access using **JWT Authentication**
✔ REST APIs exposed using **FastAPI**
✔ **MongoDB** used as the primary database

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI (Python)
* **Database:** MongoDB (Atlas)
* **ORM/Driver:** Motor (Async MongoDB driver)
* **Authentication:** JWT + bcrypt
* **API Documentation:** Swagger (OpenAPI)
* **Environment Management:** python-dotenv
* **CORS:** Enabled for frontend integration

---

## 📂 Detailed Work Breakdown

### 1️⃣ Requirement Analysis

Identified all data that needs to be stored:

* User credentials
* Text translation history
* OCR extracted and translated text
* Speech recognition results
* Chatbot conversations

✔ Chose **NoSQL (MongoDB)** for flexible multilingual and unstructured data
✔ Designed backend keeping AI & frontend integration in mind

---

### 2️⃣ Database Schema Design (Pydantic Models)

Created structured Pydantic models to ensure clean data validation and querying.

| Model           | Fields                                                            |
| --------------- | ----------------------------------------------------------------- |
| **User**        | `username`, `email`, `password`, `created_at`                     |
| **Translation** | `input_text`, `detected_lang`, `translated_text`, `user_id`       |
| **OCR**         | `extracted_text`, `detected_lang`, `translated_text`, `image_url` |
| **Speech**      | `transcribed_text`, `detected_lang`, `translated_text`            |
| **Chatbot**     | `user_message`, `bot_response`, `timestamp`                       |

➡ Ensured:

* Clean schema
* No data duplication
* Easy filtering by user ID

---

### 3️⃣ MongoDB Setup

* Created **MongoDB Atlas** cloud cluster
* Used `.env` file for secure credential storage
* Established async connection using **Motor**
* Database optimized for read-heavy history retrieval

---

### 4️⃣ Authentication System

✔ Secure user registration using **bcrypt password hashing**
✔ Login generates **JWT tokens**
✔ Protected APIs using `Authorization: Bearer <token>` headers

➡ Only authenticated users can:

* Save translation data
* Fetch personal history

---

### 5️⃣ API Endpoints (FastAPI + Routing)

#### 🔐 Authentication

* `POST /auth/register`
* `POST /auth/login`
* `GET /user/me`

#### 🌐 Translation

* `POST /translate/save`
* `GET /translate/history`

#### 🖼️ OCR

* `POST /ocr/save`
* `GET /ocr/history`

#### 🎙️ Speech

* `POST /speech/save`
* `GET /speech/history`

#### 💬 Chatbot

* `POST /chatbot/save`
* `GET /chatbot/history`

✔ Strict authentication on protected routes
✔ Centralized error handling implemented

---

### 6️⃣ Swagger, CORS & Testing

* Enabled **Swagger UI** for interactive API testing
* Configured **CORS middleware** for frontend access
* Tested all modules independently:

  * Signup & Login
  * JWT Authorization
  * History Save & Fetch APIs

✔ Verified stability before frontend & AI integration

---

### 7️⃣ Team Collaboration & Scalability

* Prepared API documentation for easy onboarding
* Designed backend to allow:

  * **AI Team** → plug in translation, OCR, speech & chatbot models
  * **Frontend Team** → fetch and save data seamlessly
* Modular structure supports future feature expansion

---

## 🚀 How to Run Locally

```bash
# Clone repository
git clone https://github.com/your-username/transly-backend.git

# Install dependencies
pip install -r requirements.txt

# Add environment variables
touch .env

# Run server
uvicorn main:app --reload
```

---

## 🏁 Conclusion

This backend provides a **secure, scalable, and modular foundation** for the Transly translation platform, ensuring smooth integration with AI models and frontend systems for **Smart India Hackathon 2025**.

---

**Developed for SIH 2025 – Transly Team** 🚀
