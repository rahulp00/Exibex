# 🎨 Exibex - AI + Real Painting Selling Website

**Exibex** is a Django-based full-stack web application that sells both original and AI-generated paintings. It includes an AI-powered chatbot, painter and user login systems, fake payment integration, and support for various AI APIs.

---
Images:

   1.Register:![image](https://github.com/user-attachments/assets/6fee58e1-c0c1-492b-bb63-65f27a001637)
   2.Login:![image](https://github.com/user-attachments/assets/323a288c-aedd-4049-bacb-073243ff6b79)
   3.Home:![image](https://github.com/user-attachments/assets/4e5c0adb-fc69-4579-9659-d6564a6016f7)
   4.AI Painting:![image](https://github.com/user-attachments/assets/0d844621-e649-45ea-8619-8074c87680f9)
   5.Painting Upload:![image](https://github.com/user-attachments/assets/d8f1eb00-84c2-45b2-a267-6dc91c9178f6)
   6.Chatbot:![image](https://github.com/user-attachments/assets/be2bc299-e06f-4e7d-91db-79d0c9d83347)
   7.Customer Quearies:![image](https://github.com/user-attachments/assets/273514d6-2b0c-4dc5-a236-430d64a4823d)
   8.View Order:![image](https://github.com/user-attachments/assets/11cd7a18-efc8-4b59-a36c-1a081d32a473)
   9.Feedback:![image](https://github.com/user-attachments/assets/438f94da-a25a-4b0d-bd01-6c198fe45ccf)


## 🛠 Tech Stack

- **Backend**: Python (Django)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default Django DB)
- **AI APIs**: 
  - [ImagePig API](https://imagepig.com)
  - [BardAPI](https://github.com/dsdanielpark/Bard-API)
  - [OpenAI API](https://platform.openai.com)

---

## 📦 Features

### 🎨 Painting Modules
- Upload and manage real paintings by painters
- Buy real or AI-generated paintings
- AI image generation using ImagePig & OpenAI
- Save generated paintings to media folder
- Add to cart / wishlist options (optional)

### 🤖 AI Features
- AI chatbot using **BardAPI** and **OpenAI**
- Interactive chatbot interface
- AI image generation (ImagePig fallback to OpenAI)

### 👥 User System
- User and Painter registration/login
- Painter dashboard for uploading and managing artworks
- User dashboard to browse, generate, and purchase

### 💳 Payment System
- Simulated/fake payment gateway for demo purposes
- Fake "Pay Now" button simulates success

---
🧠 APIs Used

📸 ImagePig API

Used to generate AI images via prompts.

Docs: https://imagepig.com/api

💬 BardAPI

Used to integrate a free chatbot experience.

GitHub: https://github.com/dsdanielpark/Bard-API

🧠 OpenAI

Fallback for high-quality image or text generation.

Docs: https://platform.openai.com/docs

---
Set Api in app1.views

![image](https://github.com/user-attachments/assets/24022f09-b792-4344-b1d5-cc1bfdcca242)

## ⚙️ Setup Instructions

```bash
git clone https://github.com/rahulp00/exibex.git

cd exibex

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver


Author

Made with by Rahul Prajapati
email: rahul38865@gmail.com


