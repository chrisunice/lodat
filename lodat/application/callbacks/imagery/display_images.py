import os
import glob
import flask
from dash.dependencies import Input, Output

from lodat.application.app import app
from lodat.application import config

list_of_images = [os.path.basename(path) for path in glob.glob(f"{config.image_folder}/*.png")]
static_image_route = '/static/'


@app.server.route('{}<image_path>.png'.format(static_image_route))
def serve_images(image_path):
    image_name = f"{image_path}.png"
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(config.image_folder, image_name)


@app.callback(
    Output('imagery-carousel', 'items'),
    Input('database-icon', 'n_clicks')
)
def display_images(click):
    if click:
        items = []
        for idx, path in enumerate(list_of_images):
            items.append(
                dict(
                    key=str(idx+1),
                    src=f'{static_image_route}{path}',
                    caption=f'{os.path.splitext(path)[0]}'
                )
            )
        return items
