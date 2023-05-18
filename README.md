### Тестовое задание Открытые Бизнес Технологии

### Добавлена возможность:
- осуществлять подписки/отписки на авторов постов.

### Использованный стек технологий:
--extra-index-url http://pypi.bars-open.ru/simple/
--trusted-host pypi.bars-open.ru

django==2.2.2
m3-django-compat==1.9.2
m3-objectpack==2.2.47
m3-ui~=2.2.106

### Настройка и запуск на компьютере
Клонируем проект:
```
https://github.com/32Aleksey32/hw05_final.git
```
Переходим в папку с проектом:
```
cd m3_project
```
Устанавливаем виртуальное окружение:
```
python -m venv venv
```
Активируем виртуальное окружение:
```
source venv/Scripts/activate
```
Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

```
Запускаем проект:
```
python manage.py runserver
```
После чего проект будет доступен по адресу http://127.0.0.1:8000/


