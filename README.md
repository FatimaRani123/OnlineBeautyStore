# 🌸 Online Beauty Store

An Online Beauty Store is a Django-based e-commerce web application that allows users to browse beauty products by category, view product details, and purchase products through a simple and user-friendly interface. The project is designed to provide a smooth online shopping experience while allowing administrators to manage products and categories efficiently.

---

## ✨ Features

- User Registration & Login
- Browse Products by Category
- Product Detail Page
- Search Products
- Shopping Cart
- Checkout System
- User Profile Management
- Admin Dashboard
- Category Management
- Product Management
- Responsive User Interface
- Environment Variable Support (.env)

---

## 🛠️ Technologies Used

### Backend
- Python 3.x
- Django 5.x
- SQLite3

### Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Other Libraries
- django-crontab
- python-dotenv

---

## 📂 Project Structure

```
OnlineBeautyStore/
│
├── catalog/
├── templates/
├── static/
├── media/
├── beauty_store/
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/FatimaRani123/OnlineBeautyStore.git
```

### 2. Navigate to Project

```bash
cd OnlineBeautyStore
```

### 3. Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📦 Requirements

The project dependencies are listed in:

```
requirements.txt
```

Main packages include:

- Django
- django-crontab
- python-dotenv

---

## 👨‍💻 Admin Panel

Access the admin dashboard at:

```
http://127.0.0.1:8000/admin/
```

Login using the superuser credentials created during setup.

---

## 📸 Screenshots

You can add screenshots here.

- Home Page
- Product Listing
- Product Details
- Shopping Cart
- Checkout
- Admin Dashboard

---

## 🚀 Future Improvements

- Online Payment Integration
- Product Reviews & Ratings
- Wishlist
- Order Tracking
- Email Notifications
- Discount Coupons
- REST API
- Product Recommendations

---

## 📄 License

This project is developed for educational and learning purposes.

---

## 👩‍💻 Author

**Fatima Rani**

GitHub:
https://github.com/FatimaRani123
