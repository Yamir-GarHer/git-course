from flask import flask

app = flask(__name__)

@app.route('/')
def index():
    return "Adios"

@app.route('/hello')
def greating():
    return "Yamir dice hola"

@app.route('/sum/<int:a>/<int:b>')
def sum(a:int,b:int):
    nums_sum = a + b
    return str(nums_sum)