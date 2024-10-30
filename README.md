# PKMApiDevelop

---

# 🚀 Запуск проекта

## 📥 Клонирование проекта
1. Перенесите проект в удобное локальное расположение с GitHub.

## 🛠️ Открытие проекта
2. Откройте проект в любой удобной IDE (рекомендуется **VSCode**).

## 🌐 Установка и активация виртуального окружения
Предварительно убедитесь, что Python установлен на вашем компьютере.

### 🔹 Windows
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```

### 🔹 Unix-подобные системы (Linux/macOS)
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

## 📦 Установка зависимостей
После активации виртуального окружения установите необходимые пакеты:
```bash
pip install django
pip install djangorestframework
pip install psycopg2
pip install django-storages
```

## 🏃 Запуск сервера
Перейдите в консоли в папку с файлом `manage.py`:
```bash
cd {dir_name}
```
Запустите сервер командой:
```bash
python manage.py runserver
```
(Или `python3 manage.py runserver` на Unix-подобных системах)

## 👤 Создание администратора
Находясь в той же директории, создайте администратора командой:
```bash
python manage.py createsuperuser
```
(Или `python3 manage.py createsuperuser` на Unix-подобных системах)

## 🔑 Доступ к панели администратора
1. Запустите сервер и откройте браузер.
2. Перейдите по адресу:
   ```
   http://127.0.0.1:8000/admin/
   ```
3. Введите учетные данные, созданные при выполнении команды `createsuperuser`.

---

# 📚 PKMApi Documentation

## 📋 Общие положения
Все обращения к серверу осуществляются посредством шаблонного запроса к бэкенду:

```
{Server_IP}:{Port}/api/{version}/{query_tag}/
```

### 🔍 Примеры запросов:
- **JSON формат вывода:**
  ```
  127.0.0.1:8000/api/v1/orderlist/?format=json
  ```
- **API формат вывода для проверки статуса (только для администраторов):**
  ```
  127.0.0.1:8000/api/v1/orderlist/?format=api
  ```

## 🚀 Доступные запросы для роли "Плановик"

### 🔹 GET-запросы:
- **Вывод заказов на производство:** 
  ```
  /api/v1/orderlist
  ```
- **Вывод распределения партий:** 
  ```
  /api/v1/batchlist
  ```

--- 
