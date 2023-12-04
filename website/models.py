from .import db  

from flask_login import UserMixin

from sqlalchemy.sql import func

    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    cnpj = db.Column(db.String(150))
    password = db.Column(db.String(150))
    password = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    estabelecimento = db.relationship('Estabelecimentos')

    def to_json(self):
        return {
                "id": self.id, 
                "email": self.email,
                "cnpj": self.cnpj,
                "password": self.password
        
                }
    

class Estabelecimentos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    endereco = db.Column(db.String(150))
    telefone = db.Column(db.String(120))
    hora_func = db.Column(db.String(120))
    descricao = db.Column(db.Text)
    foto = db.Column(db.Text)
    fotob = db.Column(db.Text)
    fotoc = db.Column(db.Text)
    fotod = db.Column(db.Text)
    user_fk = db.Column(db.Integer, db.ForeignKey("user.id"))
    servicos = db.relationship('Comercios_item')
    comercios_item = db.relationship('Servicos')

    def to_json(self):
        return {
                "id": self.id, 
                "nome": self.nome,
                "endereco": self.endereco,
                "telefone": self.telefone,
                "hora_func": self.hora_func,
                "descricao": self.descricao,
                "foto": self.foto,
                "fotob": self.fotob,
                "fotoc": self.fotoc,
                "fotod": self.fotod,
                
                "user_fk": self.user_fk
                }




class Comercios_item(db.Model, UserMixin):
    item_id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150))
    nome = db.Column(db.String(150))
    marca = db.Column(db.String(150))
    quantidade = db.Column(db.String(150))
    peso = db.Column(db.String(150))
    valor = db.Column(db.String(10))
    fim_promo = db.Column(db.String(150))
    foto = db.Column(db.Text, nullable =False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    estab_fk = db.Column(db.Integer, db.ForeignKey("estabelecimentos.id"))
    
    def to_json(self):
        return {
                "item_id": self.item_id, 
                "tipo": self.tipo,
                "nome": self.nome,
                "marca": self.marca,
                "quantidade": self.quantidade,
                "peso": self.peso,
                "valor": self.valor,
                "fim_promo": self.fim_promo,
                "foto": self.foto,
                "date": self.date,
                "estab_fk": self.estab_fk
                }


class Servicos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(150))
    descricao = db.Column(db.String(150))
    valor = db.Column(db.String(150))
    horario_func = db.Column(db.String(150))
    foto = db.Column(db.Text)
    fotob = db.Column(db.Text)
    fotoc = db.Column(db.Text)
    fotod = db.Column(db.Text)
   
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    estab_fk = db.Column(db.Integer, db.ForeignKey('estabelecimentos.id'))

    def to_json(self):
        return {
                "id": self.id, 
                "tipo": self.tipo,
                "descricao": self.descricao,
                "valor": self.valor,
                "horario_func": self.horario_func,
                "foto": self.foto,
                "fotob": self.fotob,
                "fotoc": self.fotoc,
                "fotod": self.fotod,
                "date": self.date,
                "estab_fk": self.estab_fk
                }