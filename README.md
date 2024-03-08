# Тестовое задание для SIA Konomic

## Обзор

Проект представляет собой автоматизированные тесты, разработанные с использованием языка программирования Python и инструмента автоматизации браузеров Playwright.
В проекте используется паттерн проектирования Page Object Model (POM) для улучшения читаемости и поддерживаемости кода.
Также внедрена параметризация тестов с использованием pytest для более гибкого и эффективного тестирования.

## Структура проекта

- pages/: Директория, содержащая классы страниц, реализующие POM
    - sign_up_page.py: POM страницы Регистрации
- test_data/: Директория, содержащая тестовые данные
    - sign_up_data.py: Тестовые данные для параметризации тестов страницы Регистрации
- tests/: Директория, содержащая тестовые сценарии
    - test_sign_up.py: Тесты страницы Регистрации

## Установка и запуск

Перед тем как продолжить нужно иметь установленным [Python](https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe) и [git](https://git-scm.com/download/win)

1. Клонировать репозиторий
```
git clone https://github.com/waldemirrr/sia-konomic_test_playwright.git)https://github.com/waldemirrr/sia-konomic_test_playwright.git
cd sia-konomic_test_playwright
```
2. Создать виртуальную среду и активировать её
```
python -m venv venv
source venv/bin/activate  # для UNIX/Linux
venv\Scripts\activate  # для Windows
```

