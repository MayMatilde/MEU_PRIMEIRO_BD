from flask_sqlalchemy import SQLAlchemy  #importando o database

db = SQLAlchemy()

def init_db(app):

    #configurando o database =)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///first.db "
    #criando o database:
        
  

    with app.app_context():  #db = SQLAlchemy(app)
            db.init_app(app)
            db.create_all()