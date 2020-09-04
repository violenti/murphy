from wtforms import Form
from wtforms import StringField,SelectField
from wtforms import validators

class CommentForm(Form):
    username = StringField('username',
               [
                validators.Length(min = 4, max = 25, message= 'Ingrese un usuario valido'),
                validators.DataRequired(message= 'El username es requerido')
               ]
               )
    namespace = StringField('namespace')


