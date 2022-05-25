from lodat.application.app import app
from lodat.application.layout import layout
from lodat.application.callbacks import *

if __name__ == "__main__":
    app.layout = layout
    app.run_server(debug=True, port=8888)
