# Зависимости:
1. flask
2. mysql.connector
3. python3

# Инструкция по установке:
1. `pip3 install flask`
2. `pip3 install mysql-connector-python`

# Инструкция по запуску:
0. Сделать папку с проектом рабочей.
1. Запустить сервер базы данных:

`sudo mysqld_safe --skip-grant-tables --port=3306`

2. Проинициализировать базу данных:

`echo "source init-db.sql" | sudo mysql --port=3306 --user=mysql`

3. Запустить сервер веб-приложения:

`python3 ./bankmole.py`

4. Открыть в браузере:
`http://127.0.0.1:5000/`