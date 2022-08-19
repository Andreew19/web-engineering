# WebShop
### Планы: ###



## Как запустить проект:

## Установка ##

### Клонировать репозиторий: ###
```shell
git clone https://github.com/batalova90/meeting_website/
```
### Установить виртуальное окружение: ###
```shell
python -m venv venv
```
### Включить виртуальное окружение: ###
```shell
source venv/bin/activate (macOS или Linux)
```
```shell
source venv/Scripts/activate (Windows)
```
### Установить зависимости из файла requirements.txt: ###
```shell
python -m pip install --upgrade pip
```
```shell
pip install -r requirements.txt
```

### Выполнить миграции: ###
```shell
python manage.py migrate
```
### Запустить проект: ###
```shell
python manage.py runserver
```
### Проверить, что все работает: ###
http://127.0.0.1/
