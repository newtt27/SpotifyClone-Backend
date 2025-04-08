# SpotifyClone-Backend

## 1.Tạo môi trường ảo

    python -m venv myvenv

### 1.1Sau đó chạy lệnh sau để mở quyền chạy Scripts trên PowerShell

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### 1.2Chạy môi trường ảo

    myvenv\Scripts\activate

## 2.Cài đặt các thư viện cần thiết cho project trong file requirements:

    pip install -r requirements.txt

## 3.Cấu hình lại database:

    Cấu hình lại database trong file settings.py của spotify_clone_backend
    Database dùng PostgreSQL

## 4.Runserver:

    python manage.py runserver

## Ngoài lề:

- Muốn tạo project Django: django-admin startproject 'project-name' . (Thêm dấu '.' đế tạo project trực tiép)
- Tạo các apps: python manage.py startapp 'app-name'
