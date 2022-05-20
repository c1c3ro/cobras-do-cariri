from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField, TextAreaField
from wtforms.fields import DateTimeField, DecimalField, FileField
from wtforms.validators import DataRequired

class OcorrenciaForm(FlaskForm):
    localizacao = StringField('Localização', validators=[DataRequired()])
    dataHora = DateTimeField('Data e hora', validators=[DataRequired()])
    localizacao_lat = DecimalField("Localização - Latitude")
    localizacao_log = DecimalField("Localização - Longitude")
    imagem = FileField('Imagem')
    informacao_adc = TextAreaField("Informações Adicionais")