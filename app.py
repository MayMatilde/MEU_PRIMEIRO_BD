from flask import Flask, jsonify
from models.user import User, db
from database import init_db

app = Flask(__name__)

init_db(app)

@app.route('/add')
def add():  #não é necessário passar o id, pois o bd já entende
    user = User(nome = "May", email = "may@maymay.com")
    db.session.add(user)
    db.session.commit()
    return 'Adicionado com sucesso!'

@app.route('/ver')
def ver():
    users = User.query.all()
    listaUser = []

    for user in users: 
        listaUser.append(user.toJson())

    return jsonify(listaUser)  #retornando a minha lista para json a cada rota "add" atualizada


if __name__ == "__main__":
    app.run()