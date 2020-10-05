from bottle import route, run, template

@route('/hello')
@route('/hello/<my_name>')
def get_hello(my_name="unknown person"):
    return template("Hello, {{name}}!", name=my_name)

@route('/')
def get_goodbye():
    return "<html>Goodbye there!!!</html>"

run(host='localhost', port=8080)

