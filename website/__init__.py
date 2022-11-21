from flask import Flask
from os import path
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# iniciando o banco de dados
db = SQLAlchemy()

DB_NAME = "database.db" # para o sqlite

DB_POSTGRES = "dip57lu764jvhbqp5tjry7mkyfi"
USER = 'app_rw_dciptanihirr6ym5z34g7qy2lq'
PASSWORD = 'VELVD1RL9EgBafHRQTL0Dke8KrqCLdFv'
HOST = '@pg-tunnel.borealis-data.com:65411'


def create_app():
    app = Flask(__name__)
 #Sqlite configuração
    app.config['SECRET_KEY'] = 'grhteyeuwhhs fgdhjajakuww'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
 
 #Postgres
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USER}:{PASSWORD}@{HOST}:65411/{DB_POSTGRES}'
    db.init_app(app)



    from .views import views
    from .auth import auth
    from .home import ind
    from .api.usuarios import api
    from .api.produtos import prod
    from .api.negocios import estab
    from .api.servicos import serv
    

    

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(ind, url_prefix='/')
    app.register_blueprint(api, url_prefix='/' )
    app.register_blueprint(prod, url_prefix='/' )
    app.register_blueprint(estab, url_prefix='/' )
    app.register_blueprint(serv, url_prefix='/' )
    
    

    from .models import User, Comercios_item, Estabelecimentos, Servicos

    'create_database(app)'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    with app.app_context():
         db.create_all()        
       
       
         return app
    def create_database(app):
        db.create_all(app=app)  
    if not path.exists('website/' + DB_NAME):
       db.create_all(app=app)
       print('Created Database')

   
