# Django E-Commerce Website

A web-based e-commerce application built with **Python and Django**. This project demonstrates practical backend development skills through user authentication, product management, shopping cart functionality, order processing, and payment integration.

## Features

### User Authentication & Account Management
- User registration and login
- Email-based account activation
- Password reset via email
- User profile management
- Purchase history

### Product Catalog
- Product listing and detailed product pages
- Product search and filtering by price and brand
- Product images and galleries
- Homepage slider and product sections

### Shopping Cart & Orders
- Shopping cart functionality
- Order creation and management
- ZarinPal payment integration (request and verification flow)

### Articles & Content
- Article listing and detail pages
- Contact page
- User panel
- Django admin integration for content and data management

## Technologies

- **Backend:** Python, Django, Django ORM
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (local development)
- **Email:** SMTP
- **Payment:** ZarinPal
- **Version Control:** Git and GitHub

## Project Structure

The project is organized into separate Django applications:

- `account_module` — user accounts and authentication
- `product_module` — product catalog and product details
- `article_module` — article content
- `contact_module` — contact functionality
- `user_panel_module` — user panel and purchase history
- `order_module` — shopping cart, orders, and payment processing
- `home_module` — homepage functionality
- `site_module` — general website functionality

## Getting Started

### Prerequisites
- Python 3.11 or compatible version
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Azadian-mh/django-ecommerce-v2.git
   cd django-ecommerce-v2
   ```

2. Create and activate a virtual environment:

   **Windows (PowerShell):**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **Linux / macOS:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and configure the required environment variables.

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000/ in your browser.

## Environment Configuration

Create a `.env` file in the same directory as `manage.py`:

```dotenv
SECRET_KEY=your_django_secret_key
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
```

Replace the example values with your own credentials. Never commit the `.env` file or expose real credentials in the repository.

Email functionality requires valid SMTP settings.

## Security Notes

- Sensitive credentials are stored in environment variables.
- The local SQLite database and virtual environment are excluded from version control.
- For production deployment, configure appropriate security settings, a production-ready database, HTTPS, and secure email credentials.

## Project Status

This project is a portfolio project demonstrating practical Django web application development. Further improvements and features may be added over time.