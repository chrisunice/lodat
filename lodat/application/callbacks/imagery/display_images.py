import os
import flask
import pandas as pd
from dash.dependencies import Input, Output, State

import lodat as lo
from lodat.application.app import app
from lodat.application import config

import sqlite3

db = sqlite3.connect(config.imagery_database_path)
list_of_images = [os.path.basename(path) for path, in db.execute("SELECT ImagePath FROM data")]
static_image_route = '/static/'


# This code looks to run when the flask server is started and it routes the files
# from the local machine to the /static folder
# NOTE this code may need to be moved into the callback and serve the images once the callback fires
@app.server.route('{}<image_path>.png'.format(static_image_route))
def serve_images(image_path):
    image_name = f"{image_path}.png"
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(config.image_folder, image_name)


# On the callback firing the images that are now in the /static folder can be displayed
@app.callback(
    Output('imagery-carousel', 'items'),
    Output('imagery-store', 'data'),
    Input('imagery-sidebar-submit-button', 'n_clicks'),
    State('platform-dropdown', 'value'),
    State('band-dropdown', 'value'),
    State('polarization-dropdown', 'value'),
    State('look-center-input', 'value'),
    State('look-tolerance-input', 'value'),
    State('depression-center-input', 'value'),
    State('depression-tolerance-input', 'value'),
    prevent_initial_call=True,
)
def display_images(submit_click, plats, bands, pols, look_center, look_span, depr_center, depr_span):
    if submit_click:

        dbm = lo.ImageryDatabaseManager()
        # l0, l1 = look_center-look_span, look_center+look_span
        # d0, d1 = depr_center-depr_span, depr_center+depr_span
        # results = dbm.query(plats, bands, pols, l0, l1, d0, d1)
        results = pd.read_sql("SELECT * FROM data", dbm.conn)

        items = []
        for idx, path in enumerate(list_of_images):
            items.append(
                dict(
                    key=str(idx+1),
                    src=f'{static_image_route}{path}',
                )
            )
        return items, results.to_dict('records')
