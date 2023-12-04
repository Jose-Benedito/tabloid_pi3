from website import create_app
from flask import Flask, session
import os

app = create_app()
app.secret_key = "super secret key"

def pagina_no_encontrada(error):
    return "<h1>A página que procura no existe...</h1>",404

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)
    