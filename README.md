### Тестовое задание Открытые Бизнес Технологии

Выполненые задачи:

Создан и развёрнут django-проект с подключённым рабочим столом m3;
Реализован GUI интерфейс CRUD операций для моделей:
ContentType;
User;
Group;
Permission.

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
Клонируе проект
git@github.com:makhotin07/test_m3project.git
```
Запускаем проект:
```
python manage.py runserver
```
После чего проект будет доступен по адресу http://127.0.0.1:8000/


