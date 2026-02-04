## 🏘 OpenMahalla API
• OpenMahalla is a backend REST API designed to digitalize the process of submitting, reviewing, and answering citizen appeals at the mahalla (local community) level.

• The project is built with Django REST Framework and secured using JWT authentication, following real-world backend architecture principles.

## 🌐 Live Swagger API Documentation

👉 https://openmahalla.uz/

## 📌 Project Purpose
**The goal of this project is to replace traditional (paper-based or verbal) appeals with a:**

• Structured

• Transparent

• Manageable

online system that improves communication between citizens and local administrations.

## 🛠 Tech Stack

🐍 Python 3.13

🌐 Django 6.0

🔁 Django REST Framework

🗄️ PostgreSQL

🔑 JWT (SimpleJWT)

🐳 Docker & Docker Compose

📘 Swagger (drf-yasg)

## 🚀 Key Features

🔐 Secure JWT Authentication

👥 Role-based access control (Applicant / Staff / Admin)

📨 Appeal lifecycle management

🏘 Mahalla management system

🐳 Dockerized deployment

📚 Fully documented API (Swagger & Redoc)

🧱 Clean layered backend architecture

## 👤 User Roles & Permissions

**Applicant :**

• Register & login

• Create appeals

• Edit/Delete appeals only when status is new

• View only own appeals

**Staff :**

• View all appeals

• Change appeal status

• Provide official answers

**Admin / Superuser :**

• Full system control

• User management

• Appeal & Mahalla management

**🔒 Object-level permissions ensure users can modify only their own appeals and only in allowed states.**

## 🗂️ Core Domain Models

👤 User — custom authentication model with roles

📝 Appeal — citizen requests with status tracking

🏷️ Category — classification of appeals

🏘️ Mahalla — local administrative units

## 🔐 Security

🔑 JWT-based API authentication

🛂 Role-based and object-level permissions

🧑‍💼 Secure Django Admin Panel

🚫 Protected endpoints by user role

## 📌 API Documentation

All endpoints are documented using Swagger UI.
