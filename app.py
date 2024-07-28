from flask import Flask, render_template, request, redirect, url_for, session

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

username = 'root'
server = 'viaduct.proxy.rlwy.net:13519'
senha = 'eldtOEyLNXMbXWARyaTcEfYppMoBzDcv'
db = 'railway'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{senha}@{server}/{db}'

db = SQLAlchemy(app)

class usuario(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(50))
  senha = db.Column(db.Integer)

  def __init__(self, email , senha):
    self.email = email
    self.senha = senha

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
  if request.method == 'POST':
    email = request.form['email']
    senha = request.form['senha']

    dados = usuario(email = email,
       senha = senha )
    db.session.add(dados)
    db.session.commit()
    return redirect(url_for('lista'))

  return render_template("cadastro.html")

@app.route("/lista")
def lista():
    return render_template("dados.html", usuarios=usuario.query.all())


if __name__ == '__main__':
  with app.app_context():
      db.create_all()
  app.run(host='0.0.0.0', debug=True)