# Stripe Integration

ranks

## Установка

```sh
https://github.com/staffluck/ranks.git
pip(venv) install -r requirements.txt
Установки переменных окружения по шаблону .env.template в корне проекта в файле .env
```

## Запуск
```sh
python manage.py runserver 5000
```

## Эндпоинты
```sh
[GET] http://127.0.0.1:1111/buy/<int:pk>/ - Получение stripe session_id
[GET] http://127.0.0.1:1111/item/<int:pk>/ - Карточка товара с кнопкой покупки
```

