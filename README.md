# Vue Django SPA (API Integration)

## 📌 About the Project

This project demonstrates the integration of **Vue.js** and **Django** using **Django REST Framework** (DRF). The focus is primarily on backend and API development rather than frontend design. The project follows a **Single Page Application (SPA)** architecture where page transitions occur without refreshing the entire page.

### ✨ Features:
- Create, edit, and delete posts (referred to as "questions" in the codebase)
- Posts are displayed dynamically without full-page reloads
- Uses **JWT (JSON Web Token)** for secure authentication, implementing both **access** and **refresh tokens**
- Automatic token generation upon user login

### 📌 Project Structure
- **Root Directory**: Contains the **Django Backend** code
- **`frontend/` Directory**: Contains the **Vue.js** frontend code

### 📌 How to Run the Project

1. **Clone the Repository:**
```sh
git clone https://github.com/sajad-18/vue-drf.git
```

2. **Navigate to the Project Directory:**
```sh
cd vue-drf
```

3. **Install Backend Dependencies:**
```sh
pip install -r requirements.txt
```

4. **Apply Database Migrations:**
```sh
python manage.py migrate
```

5. **Run Django Server:**
```sh
python manage.py runserver
```

6. **Navigate to the Frontend Directory:**
```sh
cd frontend
```

7. **Install Frontend Dependencies:**
```sh
npm install
```

8. **Run Vue.js Development Server:**
```sh
npm run serve
```

9. Access the project via the Vue.js server URL, typically `http://localhost:8080`

---

## 🛠 Technologies Used
- **Django** (Backend framework)
- **Django REST Framework (DRF)** (For API development)
- **Vue.js** (Frontend framework)
- **JWT Authentication** (For secure user authentication)
- **SQLite** (Default database for this project)

---

## 📝 Developer
👤 **Sajjad**  
📧 Email: [sajjad.ir8415@gmail.com](mailto:sajjad.ir8415@gmail.com)  
📌 GitHub: [github.com/sajad-18](https://github.com/sajad-18)

---

## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it.

---

## 📌 خلاصه فارسی

این پروژه ادغام Vue.js و Django با استفاده از Django REST Framework (DRF) را نشان می‌دهد. تمرکز بیشتر روی توسعه بک‌اند و API بوده و نه ظاهر پروژه. این پروژه به‌صورت یک SPA (تک صفحه‌ای) طراحی شده که صفحه‌ها بدون رفرش شدن تغییر می‌کنند.

### ✨ امکانات:
- ایجاد، ویرایش و حذف پست (که در پروژه "question" نام دارد)
- نمایش پست‌ها بدون نیاز به رفرش صفحه
- استفاده از JWT برای احراز هویت کاربران
- تولید خودکار توکن هنگام ورود کاربر

### 🚀 نصب و راه‌اندازی:
۱. کلون کردن پروژه:
```sh
git clone https://github.com/sajad-18/vue-drf.git
```
۲. نصب وابستگی‌های بک‌اند:
```sh
pip install -r requirements.txt
```
۳. اجرای مهاجرت‌های پایگاه داده:
```sh
python manage.py migrate
```
۴. اجرای سرور جنگو:
```sh
python manage.py runserver
```
۵. رفتن به دایرکتوری فرانت‌اند:
```sh
cd frontend
```
۶. نصب وابستگی‌های فرانت‌اند:
```sh
npm install
```
۷. اجرای سرور Vue.js:
```sh
npm run serve
```
۸. پروژه را در آدرس `http://localhost:8080` مشاهده کنید.

