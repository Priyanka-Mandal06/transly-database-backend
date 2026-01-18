Smart India Hackathon 2025 (Translation Application (Transly database backend))
Module	                    What it stores
User Auth System	          Signup/Login, Authentication
Translation History	        Text input + translated output
OCR History	                Image → extracted text → translated text
Speech History	            Audio → recognized text → translated output
Chatbot History	            User messages & chatbot responses

✔ All data stored per user
✔ Secure access using JWT authentication
✔ FastAPI used to expose REST API endpoints
✔ MongoDB used as the primary database
Full Detailed Work Breakdown (Step-by-Step)

1️⃣ Requirement Analysis
•	Identified data that needs to be stored:
o	User credentials
o	OCR results
o	Speech recognition texts
o	Text translation
o	Chatbot conversation
Decided NoSQL structure for flexible multilingual content

2️⃣ Planned Database Schema (Data Models)
Created Pydantic models for:
Model	Fields
User	username, email, password, created_at
Translation	input_text, detected_lang, translated_text, user_id
OCR	extracted_text, detected_lang, translated_text, image_url
Speech	transcribed_text, detected_lang, translated_text
Chatbot	user_message, bot_response, timestamp
➡ Ensured clean structure, easy querying, no duplication

3️⃣ MongoDB Setup
✔ Created MongoDB Atlas cluster
✔ Stored credentials securely using .env
✔ Connection using Motor (async MongoDB driver)

4️⃣ Implemented Authentication System
•	Secure signup using password hashing (bcrypt)
•	Login generates JWT token for secure access
•	API protection using Authorization headers
➡ Ensured only logged-in users can access their history

5️⃣ Created All Required API Endpoints (FastAPI + Routing)
✔ POST /auth/register
✔ POST /auth/login
✔ GET /user/me
✔ /translate/save, /translate/history
✔ /ocr/save, /ocr/history
✔ /speech/save, /speech/history
✔ /chatbot/save, /chatbot/history
➡ Strict authentication applied on protected routes
➡ Error handling added for every request

6️⃣ Swagger + CORS + Testing
•	Enabled interactive Swagger testing
•	Configured CORS for frontend integration
•	Successfully tested:
o	Register/Login
o	Token authorization
o	All history saving/retrieval
•	Ensured all modules work independently before integration

7️⃣ Team Collaboration
•	Prepared documentation for all endpoints
•	Ensured proper backend structure to allow:
o	AI team → plug in models easily
o	Frontend team → fetch/save data smoothly
