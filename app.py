from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
db = SQLAlchemy()
db.init_app(app)

class Usuarios(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(40), nullable=False, unique=True)

    def __repr__(self):
        return f"<{self.nome}"

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    with app.app_context():
        #----adicionando dados---
        
        #user = Usuarios(nome='Baby Shark')
        #db.session.commit()  #não se esquecer dele
        #db.create_all()

        #---obtendo dados--
        
        #usuarios = db.session.query(Usuarios).all() #query= requisão para o banco de dados  #all()= tudo da tabela 
        #for user in  usuarios:
        #   print(f"Usuario: {user.id }")
        #print(usuarios)

        #---filtrando apenas um dado do banco---
       
       # user = db.session.query(Usuarios).filter_by(id=3).first()
       # print(user)

       #---alterando os dados--- 
        
        #user = db.session.query(Usuarios).filter_by(id=3).first()
        #user.nome = "Maria Helena"
        #db.session.commit()

        #---deletando dados no banco---
        user = db.session.query(Usuarios).filter_by(id=3).first()
        db.session.delete(user)
        db.session.commit()

        

    app.run(debug=True)