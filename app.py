from website import create_app
import os, sys

import logging


app = create_app()
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

def pagina_no_encontrada(error):
    return "<h1>A página que procura no existe...</h1>",404

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)
    