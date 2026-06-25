<div align="center">

# Google Form Clone

**A full-stack Google Forms clone — create forms, share via email, collect responses, and export to Excel**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-REST_Framework-092E20?style=flat&logo=django&logoColor=white)](https://djangoproject.com)
[![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=flat&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## Overview

A fully functional clone of Google Forms built with a **separate Django REST API backend** and a **Django template-based frontend**. Users can register, create forms with custom questions, share them via encrypted email links, view response analytics with graphs, and export all responses to Excel.

---

## Features

- **Form builder** — create forms with custom questions stored as structured JSON
- **JWT authentication** — secure token-based login and registration
- **Encrypted share links** — share forms via email with Fernet-encrypted URLs
- **Form expiry** — set an expiry date on any form
- **Response collection** — respondents fill forms through a public link (no login required)
- **Response analytics** — visualize answers with charts
- **Excel export** — download all responses for a form as a `.xlsx` file
- **REST API** — clean, documented API consumed by the frontend

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend framework | Django + Django REST Framework |
| Authentication | JWT (`djangorestframework-simplejwt`) |
| Data export | pandas + openpyxl |
| Encryption | Fernet (cryptography) |
| Email | Django's built-in email backend (SMTP) |
| Frontend | Django templates + HTML/CSS/JS |
| Database | SQLite (dev) / PostgreSQL (prod) |

---

## Project Structure

```
google_form_clone/
├── backend/                    # REST API Django project
│   ├── backend/                # Project config (settings, urls, wsgi, asgi)
│   ├── forms/                  # Forms & responses app
│   │   ├── models.py           # Form, Response models
│   │   ├── serializers.py      # DRF serializers
│   │   ├── views.py            # API views + Excel export + email
│   │   ├── utils.py            # Fernet encryption helpers
│   │   └── urls.py
│   ├── user/                   # User auth app (JWT)
│   ├── manage.py
│   └── db.sqlite3
│
└── frontend/                   # Template-based Django project
    ├── frontend/               # Project config
    ├── accounts/               # Login, register, profile pages
    ├── forms/                  # Form creation & response UI
    ├── templates/              # HTML templates
    ├── manage.py
    └── db.sqlite3
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/shan19990/google_form_clone.git
cd google_form_clone
```

### 2. Set up the Backend

```bash
cd backend

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Fill in your values in .env

# Apply migrations
python manage.py migrate

# Start the backend server (runs on port 8000)
python manage.py runserver
```

### 3. Set up the Frontend

Open a **second terminal**:

```bash
cd frontend

# Activate the same (or a new) virtual environment
venv\Scripts\activate

# Apply migrations
python manage.py migrate

# Start the frontend server (runs on port 8001)
python manage.py runserver 8001
```

Visit [http://127.0.0.1:8001](http://127.0.0.1:8001) in your browser.

---

## Configuration

Copy `backend/.env.example` to `backend/.env` and set:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` for development |
| `ALLOWED_HOSTS` | Comma-separated allowed hostnames |
| `ENCRYPTION_KEY` | Fernet key for encrypting share links — generate with `python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())"` |
| `EMAIL_HOST` | SMTP host (e.g. `smtp.gmail.com`) |
| `EMAIL_PORT` | SMTP port (e.g. `587`) |
| `EMAIL_HOST_USER` | Your email address |
| `EMAIL_HOST_PASSWORD` | Your email password or app password |
| `EMAIL_USE_TLS` | `True` |

---

## API Endpoints

### Forms

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/forms/create/` | Required | Create a new form |
| `GET` | `/forms/` | Required | List all forms |
| `GET` | `/forms/<id>/` | — | Get a single form |
| `PUT` | `/forms/<id>/` | Required | Update a form |
| `DELETE` | `/forms/<id>/` | Required | Delete a form |
| `GET` | `/forms/user/` | Required | List forms created by the logged-in user |
| `POST` | `/forms/send-mail/` | Required | Email a form link to recipients |
| `GET` | `/forms/<id>/export/` | Required | Download responses as `.xlsx` |

### Responses

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| `POST` | `/responses/create/` | — | Submit a response to a form |
| `GET` | `/responses/<id>/` | Required | Get a specific response |

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/user/register/` | Register a new user |
| `POST` | `/user/token/` | Obtain JWT access + refresh tokens |
| `POST` | `/user/token/refresh/` | Refresh the access token |

---

## Usage

1. **Register / Log in** on the frontend.
2. **Create a form** — add a title, expiry date, and custom questions.
3. **Share the form** — enter recipient email addresses; they receive an encrypted link.
4. **Collect responses** — respondents fill out the form without needing an account.
5. **Analyse responses** — view charts and summaries on the responses page.
6. **Export to Excel** — download a `.xlsx` file of all responses with one click.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Shankhanil Ghosh** — [GitHub](https://github.com/shan19990)
