## 🏘 OpenMahalla API
• OpenMahalla is a scalable REST API that digitizes citizen appeals and communication with local community (Mahalla) administrations.

• Built with Django REST Framework, secured via JWT authentication, and designed using clean architecture principles.

## 🛠 Tech Stack

**Language:**	Python 3.13

**Framework:**  Django 6, Django REST Framework

**Database:**	PostgreSQL

**Authentication:** JWT (SimpleJWT), Djoser

**API Docs:**	Swagger (drf-yasg), Redoc

**DevOps:**	Docker, Docker Compose, Nginx

## 🚀 Key Features

🔐 Secure JWT Authentication

👥 Role-based access control (Applicant / Staff / Admin)

📨 Appeal lifecycle management

🏘 Mahalla management system

📚 Fully documented API (Swagger & Redoc)

🧱 Scalable & maintainable architecture

##👤 User Roles & Permissions

**Applicant**

• Register & login

• Create appeals

• Edit/Delete appeals only when status is new

• View only own appeals

**Staff**

• View all appeals

• Change appeal status

• Provide official answers

**Admin / Superuser**

• Full system control

• User management

• Appeal & Mahalla management
