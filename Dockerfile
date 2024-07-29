# Используйте официальный образ Python как базовый
FROM python:3.10

# Установите рабочий каталог
WORKDIR /app


# Скопируйте файл зависимостей
COPY requirements.txt .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте весь проект в рабочий каталог
COPY . .

# Установите переменную окружения для FastAPI
ENV UVICORN_CMD="uvicorn app.main:app --host 0.0.0.0 --port 8000"

# Запустите приложение
CMD ["sh", "-c", "$UVICORN_CMD"]

RUN echo $UVICORN_CMD
