from flask import Flask, request, current_app, Response
from mysql.connector import connect, Error

app = Flask(__name__)

def loadPage(filename, mode = 'r'):
    with open(filename, mode) as file:
        page = file.read() 
    return page

def makeRequest(query):
    response = []
    try:
        connection = connect(user = "mysql", port = 3306, database="bankmole")
        cursor = connection.cursor()
        cursor.execute(query)
        for line in cursor:
            response.append(list(line))
    except Error as e:
        print(e)
    
    return response

def makeTable(data, headers):
    table = "<table><tr>"
    for h in headers:
        table += "<th>" + h + "</th>"
    table += "</tr>"

    for row in data:
        table += "<tr>"
        for el in row:
            table += "<td>" + str(el) + "</td>"
        table += "</tr>"

    table += "</table>"
    
    return table

def makePage(filename, table):
    page = loadPage(filename)
    
    header = page[:page.find("%RESPONSE%")]
    footer = page[page.find("%RESPONSE%") + len("%RESPONSE%"):]
    page = header + table + footer

    return page

@app.route('/fonts/arounder.ttf')
def arounderFont():
    return Response(loadPage('./fonts/arounder.ttf', 'rb'), mimetype='font/ttf')

@app.route('/css/style.css')
def style():
    return Response(loadPage('./css/style.css'), mimetype='text/css')

@app.route('/')
def index():
    return loadPage('./pages/index.html')

'''
Веб-приложение должно по url "/users" отдавать страницу со списком 
АКТИВНЫХ пользователей, на каждой строке списка должен быть id, имя 
пользователя. Оформить список можно как bullet list или таблицу или 
как хотите, главное, чтобы данные пользователей были на разных 
строках и чтобы смотреть было не больно. Данные для списка должны 
получаться SQL-запросом из базы (SELECT), а не быть вписанными 
в код вручную, то есть, если добавить в базу еще одного активного 
пользователя, он должен появиться при следующем заходе на страницу 
в списке. Определять активный пользователь или нет должен SQL-запрос 
по значению поля "status".
'''
@app.route('/users')
def activeUsers():
    req = makeRequest("select id, login from users where status = 1;")
    table = makeTable(req, ['id', 'login'])
    page = makePage('./pages/active.html', table)
    return page
    

'''
Должна быть выборка пользователей по login и id, данные в ней должны 
быть такие же как в выборке всех пользователей по "/users". Параметр, 
по которому должен отбираться пользователь, передается в параметре 
query string. То есть:

    по url "/by-login?login=admin" должна выдаваться страница с данными 
    пользователя c именем "admin". Ну и если не "admin" а другое имя, 
    то инфа о пользователе с таким именем, а если такого пользователя 
    не существует, то пусть что угодно происходит (хоть ошибка, хоть 
    пустая страница)

    по url "/by-id?id=3" должны выдаваться данные пользователя с id=3 и т.д.
'''
@app.route('/by-login', methods=['GET'])
def usersByLogin():
    login = request.args.get('login')
    page = makePage('./pages/by_login.html', "")

    if login != None:
        req = makeRequest("show columns from users;")
        headers = [x[0] for x in req]

        req = makeRequest("select * from users where login = \"" + str(login) + "\";")
        table = makeTable(req, headers)
        page = makePage('./pages/by_login.html', table)

    return page

@app.route('/by-id', methods=['GET'])
def usersById():
    userid = request.args.get('id')
    page = makePage('./pages/by_id.html', "")

    if userid != None:
        req = makeRequest("show columns from users;")
        headers = [x[0] for x in req]

        req = makeRequest("select * from users where id = \"" + str(userid) + "\";")
        table = makeTable(req, headers)
        page = makePage('./pages/by_id.html', table)

    return page

if __name__ == "__main__":
    app.run()