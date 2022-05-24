from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, TextAreaField, TimeField
from wtforms.fields import DateTimeField, DecimalField, FileField
from wtforms.validators import DataRequired

class OcorrenciaForm(FlaskForm):
    enviar = SubmitField("Enviar ocorrência")
    """ localizacao = StringField('Localização', validators=[DataRequired()])
    data = DateTimeField('Data', validators=[DataRequired()])
    hora = TimeField('Hora')
    localizacao_lat = DecimalField("Localização - Latitude")
    localizacao_log = DecimalField("Localização - Longitude")
    imagem = FileField('Imagem')
    informacao_adc = TextAreaField("Informações Adicionais") """