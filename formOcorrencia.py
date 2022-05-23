from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, TextAreaField
from wtforms.fields import DateTimeField, DecimalField, FileField
from wtforms.validators import DataRequired

class OcorrenciaForm(FlaskForm):
    localizacao = StringField('Localização', validators=[DataRequired()])
    data = DateTimeField('Data', format='%d/%m/%Y', validators=[DataRequired()])
    hora = DateTimeField('Hora', format= '%H:%M')
    localizacao_lat = DecimalField("Localização - Latitude")
    localizacao_log = DecimalField("Localização - Longitude")
    imagem = FileField('Imagem')
    informacao_adc = TextAreaField("Informações Adicionais")