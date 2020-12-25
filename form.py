from wtforms import Form
from wtforms import StringField,SelectField
from wtforms import validators

class CommentForm(Form):
    username = StringField('user name',
               [
                validators.Length(min = 4, max = 25, message= 'Ingrese un usuario valido'),
                validators.DataRequired(message= 'El username es requerido')
               ],render_kw={"placeholder": "usuario"}
               )
    namespace = StringField('namespace',render_kw={"placeholder": "namespace"})
    rols = SelectField(u'Rol', choices=[('view'), ('edit'), ('admin')])


