# Rtf-tube

## Запуск
Настроить .env
```
cat .env.example > .env
```
Установка зависимостей python3.12
```console
pip install -r requirements.txt
```
Запуск
```console
python3 rtf_tube/manage.py migrate
python3 rtf_tube/manage.py collectstatic
python3 rtf_tube/manage.py runserver
```