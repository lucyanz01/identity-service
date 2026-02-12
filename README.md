# CoreAuth API

A lightweight authentication system built with Flask and MariaDB.
It provides user registration, login, password hashing, and JWT-based authentication using a modular backend architecture.

## Overview

CoreAuth is a backend-focused authentication project designed to demonstrate:

* Clean Flask project structure
* JWT authentication
* Password hashing and verification
* Separation of concerns (routes, security, database, CRUD)
* REST API design

A minimal frontend is included to test authentication flows visually.

## Project Structure

```
coreauth-api/
│
├── backend/
│   └── src/
│       ├── routes/
│       │   └── auth.py        # Authentication endpoints
│       ├── security/
│       │   ├── hash.py        # Password hashing logic
│       │   └── tokens.py      # JWT creation and validation
│       ├── crud.py            # Database operations
│       ├── schemas.py         # Data validation schemas
│       ├── database.py        # DB connection/session
│       └── app.py             # Flask entry point
│
├── frontend/
│   └── index.html             # Simple UI for login/register
│
└── requirements.txt
```

## Features

* User registration with hashed passwords
* Secure login with credential verification
* JWT access token generation
* Protected route example (`/auth/me`)
* MariaDB integration via SQLAlchemy
* Simple frontend for testing authentication flows

## Tech Stack

* Python 3
* Flask
* SQLAlchemy
* MariaDB
* JWT (JSON Web Tokens)
* Tailwind CSS (frontend)

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/lucyanz01/identity-service.git
cd coreauth-api/backend
```

### 2. Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file or export variables manually:

```
export SECRET_KEY=your_secret_key
export DATABASE_URL=mysql+pymysql://user:password@localhost/dbname
```

### 5. Run the backend

From the `backend` folder:

```
python3 -m src.app
```

The server will start at:

```
http://127.0.0.1:5000
```

### 6. Open the frontend

Open in your browser:

```
frontend/index.html
```

Or serve it with any static server.

## API Endpoints

### Register

```
POST /auth/register
```

Body:

```json
{
  "email": "user@example.com",
  "password": "password123",
  "username": "user"
}
```

### Login

```
POST /auth/login
```

Body:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Response:

```json
{
  "access_token": "jwt_token_here"
}
```

### Protected route

```
GET /auth/me
```

Requires Authorization header:

```
Authorization: Bearer <token>
```

## Design Decisions

* Authentication logic is isolated in `security/` to separate cryptography and token handling from routing.
* Routes are organized using Flask Blueprints for modularity.
* CRUD operations are abstracted to keep route handlers clean.
* Schemas validate incoming data before database interaction.

## Limitations

* No production deployment configuration included
* Minimal frontend intended only for testing
* Basic error handling

## Future Improvements

* Dashboard

## License

MIT

