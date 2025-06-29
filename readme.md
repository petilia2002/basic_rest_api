# Flask Blog API

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-orange.svg)
![REST](https://img.shields.io/badge/API-REST-brightgreen.svg)

Серверная часть блога с REST API для управления постами, включая загрузку изображений.

## 📌 Особенности

- Полноценное CRUD API для постов
- Загрузка изображений с валидацией
- Модульная архитектура (Services/Controllers/Routes)
- Гибкая обработка JSON и form-data
- Автоматическая генерация уникальных имен файлов
- Конфигурация через environment variables

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.9+
- PostgreSQL (или SQLite для разработки)