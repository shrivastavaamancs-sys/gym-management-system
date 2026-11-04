# 🏋️‍♂️ Gym Management System (Django Full-Stack & API)

A full-stack, enterprise-grade Gym Management System built using **Django 6.0**, featuring a modern, multi-page frontend, automated discount calculation logic, and secure **JWT (JSON Web Token)** authentication APIs.

---

## 🚀 Key Features

* **Modern Multi-Page Frontend**: Responsive design featuring a Home page with an **automatic image slider**, About Us, Health & Wellness tips, Service plans, Expert Trainers details, and an interactive **Contact Us form with embedded Google Maps**.
* **Core Data Models**: Structured relational schema handling `Member`, `Trainer`, and `Offer` entities.
* **Automated Business Logic**: Built-in calculation methods like `get_final_fee()` for dynamic discount management.
* **REST APIs & JWT Auth**: Integrated `djangorestframework` and `djangorestframework-simplejwt` for secure token-based access (`/api/token/` and `/api/token/refresh/`).
* **Admin & Dashboard**: Complete member registration, management, and tracking workflow.

---

## 🛠️ Tech Stack

* **Backend**: Python 3.14, Django 6.0+, Django REST Framework, SimpleJWT
* **Database**: SQLite
* **Frontend**: HTML5, Advanced CSS3, JavaScript (DOM Manipulation, Carousel)
* **Tools**: Git, VS Code, Postman

---

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/shrivastavaamancs-sys/gym-management-system.git](https://github.com/shrivastavaamancs-sys/gym-management-system.git)
   cd gym-management-system


Create and activate a virtual environment:

Bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
Install dependencies:

Bash
pip install django djangorestframework djangorestframework-simplejwt
Apply database migrations:

Bash
python manage.py makemigrations
python manage.py migrate
Run the development server:

Bash
python manage.py runserver
Open your browser and navigate to: http://127.0.0.1:8000/


---

### GitHub Repo ke liye Short Description:
> **`Full-stack Gym Management System built with Django, featuring modern responsive UI, aut
