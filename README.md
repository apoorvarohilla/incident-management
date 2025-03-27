Incident Management System

Overview

This is a REST API-based Incident Management System built using Django Rest Framework (DRF) with MySQL as the database and JWT authentication. It allows users to register, log in, create incidents, and manage them securely.

Features

User Authentication (Register, Login, JWT Token Authentication)

User Profile Management (Auto-fill city/country based on PIN code)

Incident Creation & Management

Auto-generate unique incident ID (RMGxxxxx202X format)

Editable incident details (except when status = "Closed")

User can only view and manage their own incidents

Search incidents by incident ID

Technologies Used

Backend: Python, Django Rest Framework (DRF)

Database: MySQL (or PostgreSQL)

Authentication: JWT (JSON Web Tokens)

Frontend: (Optional) React.js/Postman for API testing

Installation & Setup

Prerequisites

Ensure you have Python 3.8+ and MySQL installed.

Clone the Repository

git clone https://github.com/your-username/incident-management.git
cd incident-management

Install Dependencies

pip install -r requirements.txt

Database Configuration

Edit settings.py and update MySQL credentials:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'incident_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Run Migrations

python manage.py makemigrations incidents
python manage.py migrate

Create a Superuser (Admin)

python manage.py createsuperuser

Start the Server

python manage.py runserver

The API will be available at: http://127.0.0.1:8000/

API Endpoints

Authentication

Register: POST /register/

Login: POST /login/

Refresh Token: POST /token/refresh/

User Profile

Get Profile: GET /profile/

Incident Management

Create/View Incidents: GET/POST /incidents/

Edit/Delete an Incident: GET/PUT/DELETE /incidents/<incident_id>/

Usage & Testing

Using Postman

Register a new user (/register/).

Log in to get JWT token (/login/).

Use the token in the Authorization header for subsequent requests.

Create an incident (/incidents/).

Retrieve or update incidents as needed.

Contributing

Fork the repository

Create a feature branch (git checkout -b feature-branch)

Commit changes (git commit -m 'Add new feature')

Push to your branch (git push origin feature-branch)

Open a Pull Request

License

This project is licensed under the MIT License.

Contact

For any issues or suggestions, feel free to raise an issue on GitHub or contact the project maintainer.

Happy Coding! 🚀

