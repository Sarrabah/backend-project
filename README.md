# Backend Project – Art crea pro

## 📌 Overview

This project is a little part from my personal project `Art Crea Pro` following the principles of Domain-Driven Design (DDD).

It provides a single API endpoint to create a new quote request.


## ⚙️ Tech Stack

-   **Python**
-   **Django**
-   **TokenAuthentication** for API security
-   **Role-based authorization**: `archi`, `secretary`
-   **MySQL**
-   **Make** for task automation (run server, tests, linting, migration )
-   **CI** pipeline for testing and code quality
-   **Deploy** App deployed on Azure (URL: https://artcreapro-b8bcfcc5aahfabdc.francecentral-01.azurewebsites.net/)


## 🚀 Getting Started (Run Locally)

### 1\. Clone the repository

```
git clone https://github.com/Sarrabah/backend-project.git
cd backend-project
```

### 2\. Create a virtual environment & install dependencies

```
python -m venv venv
source venv/bin/activate   # Linux
pip install -r requirements.txt
```

### 3\. Set environment variables

Create a `.env` file at the project root to store django secret key and your database information.

### 4\. Run migrations

`make makemigrations` & 
`make migrate`

### 5\. Use the Makefile to run tasks

You can automate common tasks with `make`:

`make run` Start the development server

`make test` Run all tests

`make lint` Apply code style and linting


## 🧩 API Endpoint

### Create a Quote Request

-   **URL:** `/api/quoterequest/`
-   **Method:** `POST`
-   **Authentication:** Token required
-   **Role Authorization:** Only users with role `archi` can create a new quote request
-   **Payload example:**

```
{
  "title":"First quote request",
  "description":"quote request description",
  "status":"Created"
}
```

-   **Response example:**

```
{
  "id": 1,
  "title":"First quote request",
  "description":"quote request description",
  "status":"Created"
  
}
```

### Swagger API Documentation

You can explore the full API documentation at the `/swagger` endpoint.


## 🔐 Authentication & Authorization

-   **Authentication:** TokenAuthentication (DRF)
-   **Roles:**
-   `archi` → can create quote requests
-   `secretary` → can't create quote requests
-   **Usage:**
-   Include the token in the header: `Authorization: Token your token here`

## 👩‍💻 Author

Developed by **Sarra Ben Arbia**

Feel free to run the project locally! 🚀