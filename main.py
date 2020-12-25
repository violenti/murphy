from flask import Flask
from flask import render_template
import form
from flask import request
from createuser import create

app = Flask (__name__)
@app.route('/', methods =['GET'])
def index():
    return render_template('index.html')
@app.route('/alta', methods = ['GET','POST'])

def alta():
    builduser = create
    comment_form = form.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print (comment_form.username.data)
        print (comment_form.rols.data)
        builduser(comment_form.username.data)
    return render_template('create.html', form = comment_form )

if __name__== '__main__':
    app.run(debug = True, port = 8080)

