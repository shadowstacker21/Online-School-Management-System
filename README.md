# 🏫 Online School System API

A backend API for an Online School System built with **Django REST Framework (DRF)**. This system manages departments, courses, user purchases, and role changes with secure **JWT Authentication** using **Djoser**, and includes interactive API documentation powered by **Swagger (drf_yasg)**.

---

## 🚀 Features

- 🔐 JWT Authentication (Login, Registration, Token Refresh) with **Djoser**
- 🏛️ Department Management (CRUD)
- 📚 Course Management (CRUD)
- 💰 Purchase API for course enrollment
- 🔄 Role Change API (e.g. student ↔ instructor)
- 📄 Interactive Swagger documentation
- 📦 Modular & scalable project structure
- ✅ RESTful API design principles

---

## 📁 Project Structure

online_school/
├── departments/
├── courses/
├── purchases/
├── users/
├── online_school/ # Project settings
├── manage.py

yaml
Copy code

---

## 📚 API Endpoints Overview

| Feature        | Endpoint                                 | Methods       | Auth Required |
|----------------|------------------------------------------|---------------|----------------|
| User Auth      | `/auth/users/`, `/auth/jwt/create/`      | POST, GET     | ❌ / ✅        |
| Departments    | `/api/v1/departments/`                      | GET, POST, PUT, DELETE | ✅        |
| Courses        | `/api/v1/courses/`                          | GET, POST, PUT, DELETE | ✅        |
| Purchases      | `/api/v1/courses/id/purchases/`                        | POST, GET     | ✅              |
| Role Change    | `/api/v1/user/id/change_role/`                      | POST          | ✅ (Admin)      |
| Swagger Docs   | `/swagger/`, `/redoc/`                   | GET           | ❌              |

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Django 4.x**
- **Django REST Framework**
- **Djoser** (JWT Authentication)
- **drf_yasg** (Swagger API Docs)
- **PostgreSQL** or SQLite (Configurable)

---

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/online-school.git
   cd online-school
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser (for admin access):

bash
Copy code
python manage.py createsuperuser
Run the server:

bash
Copy code
python manage.py runserver
Visit Swagger UI:

http://localhost:8000/swagger/

🧪 Example Usage (API Testing)
Use tools like Postman, cURL, or Swagger UI to interact with endpoints.

Example login (JWT):

http
Copy code
POST /auth/jwt/create/
{
  "email": "user@example.com",
  "password": "yourpassword"
}
🧰 Environment Variables
Create a .env file in the root directory for sensitive settings:

env
Copy code
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/dbname
🐳 Optional: Run with Docker
bash
Copy code
docker-compose up --build
Make sure to have a Dockerfile and docker-compose.yml configured.

🔒 Authentication Overview
Registration: /auth/users/

Login (JWT): /auth/jwt/create/

Token refresh: /auth/jwt/refresh/

Token verify: /auth/jwt/verify/

Provided by Djoser with customizations possible.

📄 API Documentation
Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/

👥 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

📜 License
MIT License

✉️ Contact
Feel free to reach out if you have any questions or suggestions!

GitHub: shadowstacker21

Email: alamincse16th@gmail.com


