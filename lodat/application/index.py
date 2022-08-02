from lodat.application.app import app
from lodat.application.layout import serve_layout
from lodat.application.callbacks import *


if __name__ == "__main__":
    app.layout = serve_layout
    app.run_server(debug=False, host="0.0.0.0", port=8050)
