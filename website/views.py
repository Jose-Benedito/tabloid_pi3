from unicodedata import category
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for, abort
from flask_login import login_required, current_user


from .models import User
from .models import Comercios_item
from .models import Estabelecimentos
from .models import Servicos


from . import db
import json

import os

"""
    Como o arquivo estará em binario será necessário essa lib para salvar
"""
from werkzeug.utils import secure_filename

UPLOAD = 'website/static/uploads/comercios'
UPLOADB = 'website/static/uploads/servicos'
UPLOADC = 'website/static/uploads/logos'

UPLOAD_FOLDER = os.path.join(os.getcwd(), UPLOAD)
UPLOAD_FOLDERB = os.path.join(os.getcwd(), UPLOADB)
UPLOAD_FOLDERC = os.path.join(os.getcwd(), UPLOADC)

views = Blueprint('views', __name__)


#-------------- Rota da home --------------------------------

@views.route('/', methods=['GET', 'POST'])
#@login_required
def home():
    dono = Estabelecimentos.query.all()
    return render_template("index.html", dono=dono, user=current_user)

################# Rotas do crud (Criar, editar, deletar)###############################

@views.route('/delete/<id>/', methods=['GET','POST'])
def delete(id):
   
    return redirect(url_for('views.admin'))
     

#-----------------------------------------------------------------------
@views.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    negocio = Estabelecimentos.query.all()
    

    if request.method == 'POST':
        nome = request.form.get('nome')
        endereco = request.form.get('endereco')
        telefone = request.form.get('telefone')
        hora_func = request.form.get('hota_func')
        descricao =request.form.get('descricao')
        
        user = request.form.get('user')
        
        file = request.files['foto']
        fileb = request.files['fotob']
        filec = request.files['fotoc']
        filed = request.files['fotod']

        namefoto = file.filename
        namefotob = fileb.filename
        namefotoc = filec.filename
        namefotod = filed.filename
        
        if file:
            savePath = os.path.join(UPLOAD_FOLDERC, secure_filename(file.filename))
            file.save(savePath)
        if fileb:
            savePath = os.path.join(UPLOAD_FOLDERC, secure_filename(fileb.filename))
            fileb.save(savePath)
        if filec:
            savePath = os.path.join(UPLOAD_FOLDERC, secure_filename(filec.filename))
            filec.save(savePath)
        if filed:
            savePath = os.path.join(UPLOAD_FOLDERC, secure_filename(filed.filename))
            filed.save(savePath)

        

        # Criar as validações dos inputs aqui

        new_item = Estabelecimentos( nome=nome, endereco=endereco, 
        telefone=telefone, hora_func = hora_func,
        descricao= descricao,foto=namefoto, fotob=namefotob, fotoc=namefotoc,
        fotod=namefotod, user_fk=user
        )


        db.session.add(new_item)
        db.session.commit()
        flash('Produto salvo com sucesso', category='success')
        return redirect(url_for('views.admin', user=current_user))
    
    return render_template("admin.html", negocio=negocio, user=current_user)

#-----------------------------------------------------------------------
@views.route('/cadastro')
def teste():
    return render_template("cadastro.html", user=current_user)

@views.route('/form/<id>', methods=['GET','POST'])
def form(id):
    dono = Estabelecimentos.query.get(id)
    

    if request.method == 'POST':
        estab_fk = request.form.get('estab_fk')
        tipo = request.form.get('tipo')
        nome = request.form.get('nome')
        marca = request.form.get('marca')
        quantidade =request.form.get('quantidade')
        peso = request.form.get('peso')
        valor = request.form.get('valor')
        
        file = request.files['foto']
       
        namefoto = file.filename
       
        if file:
        
            # salva na pasta uploads/servicos
            savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
            file.save(savePath)
        
        fim_promo = request.form.get('fim_promo')

        # Criar as validações dos inputs aqui

        new_item = Comercios_item( tipo=tipo, nome=nome, 
        marca=marca, quantidade = quantidade,
        peso= peso, valor=valor,foto=namefoto,
        fim_promo=fim_promo, estab_fk=estab_fk
        )


        db.session.add(new_item)
        db.session.commit()
        flash('Produto salvo com sucesso', category='success')
        return redirect(url_for('views.admin'))
    
    return render_template('form.html', dono=dono, user=current_user)

##-----------Formulário de serviços -------------------------------------------------##
@views.route('/form_servico/<id>', methods=['GET','POST'])
def form_servico(id):
    dono = Estabelecimentos.query.get(id)
    

    if request.method == 'POST':
        estab_fk = request.form.get('estab_fk')
        tipo = request.form.get('tipo')
        descricao = request.form.get('descricao')
        valor = request.form.get('valor')
        horario_func =request.form.get('horario_func')
       
        
        file = request.files['foto']
        fileb = request.files['fotob']
        filec = request.files['fotoc']
        filed = request.files['fotod']
        # nomes das fotos
        namefoto = file.filename
        namefotob = fileb.filename
        namefotoc = filec.filename
        namefotod = filed.filename
        # salva na pasta uploads/servicos
        if file:
            savePath = os.path.join(UPLOAD_FOLDERB, secure_filename(file.filename))
            file.save(savePath)
        if fileb:
            savePath = os.path.join(UPLOAD_FOLDERB, secure_filename(fileb.filename))
            fileb.save(savePath)
        if filec:
            savePath = os.path.join(UPLOAD_FOLDERB, secure_filename(filec.filename))
            filec.save(savePath)
        if filed:
            savePath = os.path.join(UPLOAD_FOLDERB, secure_filename(filed.filename))
            filed.save(savePath)


        # Criar as validações dos inputs aqui

        new_item = Servicos( tipo=tipo, descricao=descricao, 
        valor=valor,horario_func=horario_func, foto=namefoto, fotob=namefotob, fotoc=namefotoc,
         fotod=namefotod, estab_fk=estab_fk
        )


        db.session.add(new_item)
        db.session.commit()
        flash('Produto salvo com sucesso', category='success')
        return redirect(url_for('views.admin'))
    
    return render_template('form_servico.html', dono=dono, user=current_user)

##-----------Update de produtos -------------------------------------------------##
@views.route('/update', methods=['GET','POST'])
def update():

    return render_template('form.html', mercado=mercado, user=current_user)

@views.route("/editar/<id>/")
def editar(id):
    
    return render_template('editar.html', user = current_user)




##-----------ROTA MERCADO -------------------------------------------------##
@views.route('/mercadoa' ) #endpoints
def mercadoa ():
    
    mercado = db.session.query(Estabelecimentos).filter(Estabelecimentos.id==1)

    dados_items = db.session.query(Comercios_item).filter(Comercios_item.estab_fk==1)
    return render_template("mercadoa.html", mercado=mercado , ofertas=dados_items, comercios=comercios, user=current_user)

##-----------RODA MERCADO -------------------------------------------------##
@views.route ( '/mercadob' )
def  mercadob ():
    dados_items = db.session.query(Comercios_item).filter(Comercios_item.estab_fk==1)

    mercado = db.session.query(Estabelecimentos).filter(Estabelecimentos.id==1)
    return  render_template ( "mercadob.html",comercios=comercios,  ofertas=dados_items,  user = current_user  )

##-----------ROTA MERCADO -------------------------------------------------##
@views.route( '/mercadoc' )
def  mercado ():
     mercado = db.session.query(Estabelecimentos).filter(Estabelecimentos.id==21)

     dados_items = db.session.query(Comercios_item).filter(Comercios_item.estab_fk==1)

     return  render_template ( "mercadoc.html", comercios=comercios, ofertas=dados_items, user = current_user )

##-----------ROTA SERVIÇOS -------------------------------------------------##
@views.route( '/servicos' )
def  servicos ():
  
     return  render_template ( "servicos.html",  user = current_user )

##-----------ROTA SERVIÇOS -------------------------------------------------##
@views.route( '/servico/<id>/' )
def  servico (id):
  
     return  render_template ( "servicos.html",  user = current_user )


##------------------API DO GOOGLE MAPS---------------------------------------------

class Comercio:
    def __init__(self, key, name, lat, lng):
        self.key  = key
        self.name = name
        self.lat  = lat
        self.lng  = lng

# AS coordenadas do endereço
comercios = (
    Comercio('mercadoA',      'Mercadinho A',  -23.571319422733524, -46.414629246163614),
    Comercio('mercadoB', 'Mercadinho B',           -23.591198056010676, -46.403604962487194),
    Comercio('mercadoC',     'Mercadinho C', -23.588869063417768, -46.40864850869)
)
comercios_by_key = {comercio.key: comercio for comercio in comercios}

#GoogleMaps
@views.route("/<comercio_code>")
def show_comercio(comercio_code):
    comercio = comercios_by_key.get(comercio_code)
    if comercio:
        return render_template('map.html', comercio=comercio)
    else:
        abort(404)



