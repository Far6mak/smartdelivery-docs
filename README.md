# SmartDelivery API Documentation

## 📌 Описание проекта

SmartDelivery — учебный проект, демонстрирующий документацию REST API сервиса доставки.

Проект включает:
- описание API эндпоинтов
- Mermaid диаграммы архитектуры
- автоматические тесты API
- скрипты запуска тестов
- документацию через MkDocs

---

## 📁 Структура проекта

```
docs/
tests/
mkdocs.yml
README.md
```

---

## 🚀 Установка

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

---

## 📖 Запуск документации

### Локальный сервер:

```bash
mkdocs serve
```

Открыть в браузере:
```
http://127.0.0.1:8000
```

---

### Сборка проекта:

```bash
mkdocs build
```

---

## 🧪 Запуск тестов

### Python:

```bash
python tests/api_tests.py
```

---

### Автоматический запуск:

Linux / Mac:

```bash
bash tests/run_tests.sh
```

Windows:

```bash
tests/run_tests.bat
```

---

## 📊 Функционал API

- Создание заказа (POST)
- Получение заказа (GET)
- Обновление заказа (PUT)
- Удаление заказа (DELETE)

---

## 🧠 Технологии

- Python
- Requests
- MkDocs
- Mermaid diagrams
- REST API (JSONPlaceholder)

---

## 📈 Диаграммы

Проект содержит:
- Sequence diagram (жизненный цикл заказа)
- Flowchart обработки заказа
- Component diagram системы
- Flowchart тестирования

---

## ✅ Итог

Проект демонстрирует:
- работу с REST API
- документирование систем
- автоматизацию тестирования
- визуализацию архитектуры