from flask import Flask , render_template,request
import mysql.connector as mariadb
from flask_bootstrap import Bootstrap
app = Flask(__name__)
#mariadb_connection = mariadb.connect(host= 'localhost',port='3306', user='celdaslibres_dev', password='celdaslibres2019', database='celdas_libres')
#conexion=mysql.connector.connect(**dbconnect)
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/crearUsuario')
def crear_usuario():
    return render_template('crear_usuario.html')
@app.route('/ingresar')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=3000,debug=True)