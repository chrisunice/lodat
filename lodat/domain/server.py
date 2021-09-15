from flask import Flask
from lodat.domain import routes

server = Flask('ImageryApplication', template_folder='../application')
server.add_url_rule('/', view_func=routes.home)
server.add_url_rule('/send-images', methods=['GET'], view_func=routes.send_images)

if __name__ == '__main__':
    server.run(debug=True)
