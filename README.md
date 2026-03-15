# project-testshop-selenium

Пример реализации UI-автотестов на Selenium + Python с использованием Page Object Model

Тестируемый ресурс: http://testshop.qa-practice.com/

---
В проекте используются:

- Python
- Selenium
- Pytest
- Page Object Model (POM)
- Allure для отчетовв
---

# Установка зависимости
```
pip install -r requirements.txt
```

# Запуск тестов
```
pytest -v
```
# С отчетом Allure

```
pytest --alluredir=allure-results
allure serve allure-results
```

# Установка Allure. Windows (через Scoop)
```
scoop install allure
```
