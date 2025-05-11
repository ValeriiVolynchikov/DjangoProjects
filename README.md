# Skystore

## Описание
Skystore — это интернет-магазин для продажи плагинов и примеров кода. Проект создан на Django и использует Bootstrap для стилизации страниц.

## Функциональность
- Главная страница с информацией о сервисе.
- Страница контактов с формой обратной связи.
- Обработка формы обратной связи и вывод сообщения об успешной отправке.
- Подключение статических файлов (Bootstrap стили и скрипты).

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/ValeriiVolynchikov/DjangoProjects.git
   
   ```
2. Создайте и активируйте виртуальное окружение (рекомендуется):
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   poetry install
   ```
4. Запустите сервер разработки:
   ```sh
   python manage.py runserver
   ```
5. Откройте в браузере: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Структура проекта
```
DjangoProjects/
├── config/                # Конфигурация Django-проекта
│   ├── settings.py        # Основные настройки проекта
│   ├── urls.py            # Основные маршруты проекта
│   ├── wsgi.py            # Точка входа для WSGI
├── templates/         # HTML-шаблоны
│   ├── includes/
│   │   ├── footer.html    
│   │   ├── header.html 
│   │   ├── main_menu.html 
│   ├── admin/
│   │   ├── catalog/ 
│   │   │   ├── product/
│   │   │   │   ├── change_list.html
│   ├── home.html      # Главная страница
│   ├── base.html      # Базовый шаблон
├── catalog/               # Приложение интернет-магазина
│   ├── templates/         # HTML-шаблоны
│   │   ├── contacts.html  # Страница контактов
│   │   ├── add_product.html    
│   │   ├── product_card.html  
│   │   ├──  product_info.html
│   │   ├──  category.html
│   │   ├──  category_not_found.html
│   │   ├──  delete_product.html
│   │   ├──  edit_product.html
│   │   ├──  unpublich_product.html
│   ├── templatags/        
│   │   ├── mu_tags.py     # Файл с пользовательскими тегами
│   ├── migrations.py      # Директория приложения файлов миграции СБД
│   ├── forms.py
│   ├── services.py        # Сервисная функция для продуктов в категории
│   ├── views.py           # Контроллеры (обработка страниц и формы)
│   ├── urls.py            # Маршруты приложения
│   ├── photo/             # Папка хранения изображений продуктов
│   ├── management/        # Пакет приложения кастомной команды
│   ├───__init__.py
│       └───commands/
│           ├───__init__.py
│           └───add_products.py
│           └───clear_cache.py
├── blogs/               # Приложение БЛОГ
│   ├── templates/         # HTML-шаблоны
│   │   ├── blogs/
│   │   	├── blog_card.html      
│   │   	├── blog_create.html  
│   │   	├── base.html      # Базовый шаблон
│   │   	├── blog_delete.html  
│   │   	├── footer.html    
│   │   	├── header.html    
│   │   	├── blog_detail.html  
│   │   	├── blog_list.html
│   ├── migrations.py      # Директория приложения файлов миграции СБД
│   ├── forms.py
│   ├── views.py           # Контроллеры (обработка страниц и формы)
│   ├── urls.py            # Маршруты приложения
│   ├── models.py 
├── users/               # Приложение USERS
│   ├── templates/         # HTML-шаблоны
│   │   ├── users/
│   │   	├── login.html      
│   │   	├── profile.html  
│   │   	├── register.html 
│   │   	├── password_reset.html  
│   │   	├── password_reset_complete.html
│   │   	├── password_reset_confirm.html
│   │   	├── password_reset_done.html
│   │   	├── password_reset_email.html
│   │   	├── password_reset_subject.txt
│   │   	├── password_reset_test.html
│   │   	├──	verify_required.html    # шаблон в разработке другой ветки проекта
│   │   	├──	registration_sent.html  # шаблон в разработке другой ветки проекта
│   │   	├──	verify_email.html		# шаблон в разработке другой ветки проекта
│   ├── management/        # Пакет приложения кастомной команды
│   ├───__init__.py
│       └───commands/
│           ├───__init__.py
│           └───csu.py
│   ├── migrations.py      # Директория приложения файлов миграции СБД
│   ├── forms.py
│   ├── views.py           # Контроллеры (обработка страниц и формы)
│   ├── urls.py            # Маршруты приложения
│   ├── models.py 
│   ├── admin.py
│   ├── middleware.py	   # Для проверки верификации (опционально)	
├── static/                # Статические файлы (CSS, JS, изображения)
│   ├── css/bootstrap.min.css
|   ├── js/bootstrap.min.css
├── screenchots/           # Скриншоты выполнения Django shell
│
├── manage.py              # Основной файл управления Django-проектом
├── .env                   # Файл для хранения переменных среды и конфиденциальной информации
├── requirements.txt       # Список зависимостей
├── README.md              # Документация проекта
```

## Использование
- Перейдите на `/home/` для просмотра главной страницы.
- Перейдите на `/contacts/` для формы обратной связи.
- Заполните форму и отправьте сообщение, система уведомит об успешной отправке.

## Требования
- Python 3.8+
- Django 4+
- Bootstrap (подключается через статические файлы)

## Лицензия
Проект распространяется под свободной лицензией.
