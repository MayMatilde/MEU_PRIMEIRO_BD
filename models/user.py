from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #chave primária, tipo inteiro
    nome = db.Column(db.String(80), nullable=True) #strinf, nulo 
    email = db.Column(db.String(120), nullable=True) #strinf, nulo 

    def toJson(self):
        return {"id": self.id, "nome": self.nome, "email": self.email}