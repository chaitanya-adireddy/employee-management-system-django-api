# Django Backend API

A Django-based backend project developed as part of my learning, which includes REST APIs along with server-rendered forms and templates. The project implements authentication and permission control following real-world backend practices.

## Features
- RESTful APIs using Django REST Framework
- JWT Authentication
- User login and protected actions
- CRUD operations
- Permission control:
  - Only logged-in users can Add, Edit, and Delete data
  - Non-logged-in users can only View data
- Django Forms
- HTML Templates (server-side rendering)
- Clean and modular project structure

## Tech Stack
Python | Django | Django REST Framework | HTML | CSS | SQLite | JWT

## How to Run
```bash
git clone https://github.com/chaitanya-adireddy/employee-management-system-django.git
cd employee-management-system-django.git
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Server runs at: http://127.0.0.1:8000/

Purpose
This project was built to gain hands-on experience in Django backend development, REST APIs, authentication, permission handling, forms processing, and template rendering.

Author
Adireddy Chaitanya
ECE | Backend Developer (Python & Django)
Email: myselfadireddy@gmail.com