from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField
from wtforms.fields.html5 import EmailField, TelField
from wtforms.validators import DataRequired, Email, optional, length

class CrearUsuario(FlaskForm):
    tipo_identificacion =  SelectField('Tipo de identificación', choices=[
        ('TI', 'Tarjeta de identidad'),
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        # ...
    ], validators=[DataRequired()])
    identificacion = StringField('Identificación', validators=[DataRequired()])
    nombre1 = StringField('Primer nombre', validators=[DataRequired()])
    nombre2 = StringField('Segundo nombre', validators=optional())
    apellido1 = StringField('Primer apellido', validators=[DataRequired()])
    apellido2 = StringField('Segungo apellido', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    telefono = TelField('Teléfono fijo', validators=[DataRequired()])
    celular = TelField('Teléfono celular', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de nacimiento', format='%d/%m/%Y')
    correo = EmailField('Correo electrónico', validator=[DataRequired(), Email()])
    nacionalidad = StringField('Nacionalidad', validators=[DataRequired()])
    submit = SubmitField('Registrarme')
