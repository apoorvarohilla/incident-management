# Incident Management System

## Overview
A REST API-based **Incident Management System** using **Django Rest Framework (DRF)** and **MySQL**. Users can register, log in, create, view, and manage incidents with authentication.

## Features
- User authentication (JWT)
- Create, edit, and search incidents
- Auto-generate unique incident IDs
- Role-based access (Users manage only their incidents)
- Editable status & priority (except closed incidents)

## Tech Stack
- **Backend**: Python, Django Rest Framework
- **Database**: MySQL
- **Auth**: JWT
- **Frontend**: (Optional) React.js/Postman

## Installation
```sh
git clone https://github.com/your-username/incident-management.git
cd incident-management
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
