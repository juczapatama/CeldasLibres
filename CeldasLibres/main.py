from flask import Flask, render_template,request
from config import Config

from forms import CrearUsuario
#import mysql.connector
#import MySQLdb
#from flask_bootstrap import Bootstrap
#conexion=mysql.connector.connect(**dbconnect)
#conexion = mysql.connector.connect(host="3.90.223.62",port="3306",user="app", password="VguGqXru53BV8kIW" , database="celdas_libres")
#conexcion = MySQLdb.connect(host="3.90.223.62",port=3306,user="app",passwd="VguGqXru53BV8kIW",db="celdas_libres")
app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/crearUsuario')
def crear_usuario():
    form = CrearUsuario()
    if request.method == 'POST' and form.validate_on_submit():
        pass # Crear usuario y guardar en la BD
    return render_template('crear_usuario.html', title='Registrarme', form=form)


@app.route('/login',  methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method =='POST':
        id = request.form.get("id")
        password = request.form.get("password")
        info = str(id)+" "+str(password)
        return (info)


if __name__ == '__main__':
    app.run(port=3000,debug=True)