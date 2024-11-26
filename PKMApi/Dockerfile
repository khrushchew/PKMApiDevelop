# Используем официальный образ Python
FROM python:3.11.4-alpine

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app/

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для psycopg2
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Обновляем pip и устанавливаем зависимости из requirements.txt
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Копируем проект в контейнер
COPY . .

# Команда для запуска приложения в контейнере
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
