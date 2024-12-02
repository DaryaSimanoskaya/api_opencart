# Базовый образ Python
FROM python:3.11

# Обновление системы и установка зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Установка необходимых Python-библиотек для тестов
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование тестов в контейнер
COPY . /app
WORKDIR /app


COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh


# Установка Allure для генерации отчетов
RUN curl -o allure-2.17.3.tgz -L https://github.com/allure-framework/allure2/releases/download/2.17.3/allure-2.17.3.tgz \
    && tar -xvzf allure-2.17.3.tgz -C /opt/ \
    && ln -s /opt/allure-2.17.3/bin/allure /usr/local/bin/allure

# Установка переменных окружения
ENV URL="http://localhost:8080" \
    USERNAME="MyAPI" \
    KEY="cFdPXbk5Gzf0MrQHoz7tNBUwq6QA2olNdNsXLYweLO0LVHRySWGwVfRw8IIUMAwYwc0kPtapKcJNAjTBvQEBTzqK7m1znehsV0ugUA35tVKDC2EcnhtXuLOYZy23CmVpTbjLuZYauqCcpULQSMS0pJNZrSimx1q0mjW5NXWwvAO18PID0qjScNRzaft4L5nxCmSvA7j2PjlzME8J23oWAWVQx4Lv8eoMSx6sZ0pTBOYFSkWkKbRhcufypYxDHWx4"

# Команда для запуска тестов через Selenoid
ENTRYPOINT ["sh", "-c", "/app/wait-for-it.sh opencart 8080 pytest --url=${URL} --username=${USERNAME} --key=${KEY} --alluredir=./allure-results"]
