# Django Full Stack Data Engineer Project

## Overview
This is a demo project built with **Django**, **PostgreSQL**, and **Django REST Framework** to showcase full-stack data engineering skills. The project demonstrates:

- CRUD operations for Products stored in PostgreSQL
- Integration with a third-party API (CoinGecko) for crypto prices
- Data visualization using Plotly for both Products and Cryptocurrencies
- A REST API with a **custom API root** providing clickable links to all endpoints
- Deployment-ready structure

---

## Features

### 1. Product Management (CRUD)
- Create, Read, Update, and Delete products via REST API
- PostgreSQL database used for storing products
- Fields for each product:
  - `name` (string)
  - `description` (text)
  - `price` (float)
  - `created_at` (timestamp)

### 2. Third-Party API Integration
- Fetches **current USD prices** for 10 popular cryptocurrencies from [CoinGecko API](https://www.coingecko.com/en/api)

### 3. Data Visualization
- **Product Prices Chart:** Bar chart showing prices of all products
- **Crypto Prices Chart:** Bar chart showing current prices of 10 cryptocurrencies
- Built using Plotly for interactive visualization

### 4. API Root
- Custom API root with all endpoints clickable for easy testing

---

## Endpoints

### API Root
- [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)  
Returns JSON with clickable links to all other endpoints

### Product CRUD
- List / Create: [http://127.0.0.1:8000/api/products/](http://127.0.0.1:8000/api/products/)  
- Retrieve / Update / Delete (example ID=1): [http://127.0.0.1:8000/api/products/1/](http://127.0.0.1:8000/api/products/1/)

### Product Prices Visualization
- Bar chart: [http://127.0.0.1:8000/api/product-chart/](http://127.0.0.1:8000/api/product-chart/)

### Crypto Prices API
- Raw JSON data for 10 cryptocurrencies: [http://127.0.0.1:8000/api/crypto-prices/](http://127.0.0.1:8000/api/crypto-prices/)

### Crypto Prices Visualization
- Bar chart for 10 cryptocurrencies: [http://127.0.0.1:8000/api/crypto-chart/](http://127.0.0.1:8000/api/crypto-chart/)

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/django_demo_project.git
cd django_demo_project
```

### 2. Create a virtual environment and activate it
```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL
- Create a PostgreSQL database (example: demo_db)
- Update your demoapp/settings.py with your database credentials:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demo_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Run the development server
```bash
python manage.py runserver
```

### 7. Open the API root
- http://127.0.0.1:8000/api/

## Dependencies
- Python 3.11
- Django 5.2.6
- Django REST Framework
- psycopg2-binary
- requests
- plotly
- pandas
All dependencies are listed in requirements.txt and can be installed via:
```bash
pip install -r requirements.txt
```

--- 

## Deployment Notes
You can deploy the project live on platforms like Render.com, Railway.app, or Heroku. Suggested steps:
1. Push your code to GitHub (already done)
2. Connect the GitHub repository to the deployment platform
3. Set environment variables for PostgreSQL database:
   - DATABASE_URL (platform-provided)
4. Install build dependencies if required (Plotly, pandas)
5. Deploy and test the live URL
6. Update the API root URL in README if needed
