# 📚 Book Intelligence Platform

A full-stack AI-powered web application that allows users to explore books and ask intelligent questions about them.

---

## 🚀 Features

- 📖 View a list of books
- 🔍 Ask questions about books
- 🤖 Smart filtering based on user queries
- 🌐 REST API built with Django
- ⚛️ Interactive frontend using React

---

## 🛠 Tech Stack

- Backend: Django, Django REST Framework
- Frontend: React.js
- Database: SQLite

---

## 📸 Screenshots
<img width="1284" height="209" alt="Screenshot 2026-04-19 021043" src="https://github.com/user-attachments/assets/57be8e3c-ac8e-4010-86b6-20a65f8b1eb2" />
<img width="744" height="191" alt="Screenshot 2026-04-19 021109" src="https://github.com/user-attachments/assets/a2b3929c-60b0-4506-9823-faaade405486" />
<img width="759" height="184" alt="Screenshot 2026-04-19 021135" src="https://github.com/user-attachments/assets/0c417a36-4059-4cd1-8a21-84ff91e3ea13" />


### 💻 Frontend UI
<img width="941" height="597" alt="Screenshot 2026-04-19 021944" src="https://github.com/user-attachments/assets/c7863ed2-10d5-4c55-a961-93a7f9a7e569" />


### 📚 API Response
<img width="1300" height="624" alt="Screenshot 2026-04-19 021314" src="https://github.com/user-attachments/assets/1a017667-31cf-40b4-9b91-a39d1c14f315" />
<img width="1274" height="572" alt="Screenshot 2026-04-19 021332" src="https://github.com/user-attachments/assets/3d72a7a1-974b-419a-98eb-feb3c463f6fd" />


---

## 📌 API Response Examples

### 🔹 GET `/api/books/`

```json
[
  {
    "id": 1,
    "title": "A Light in the Attic",
    "genre": "History"
  },
  {
    "id": 2,
    "title": "Tipping the Velvet",
    "genre": "Romance"
  },
  {
    "id": 3,
    "title": "Soumission",
    "genre": "Science"
  }
]
