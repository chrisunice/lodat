import os
import glob
import flask
from dash import html
from dash.dependencies import Input, Output

from lodat.application.app import app

image_directory = "C:/LODAT/test_assets/images/"
list_of_images = [os.path.basename(x) for x in glob.glob('{}*.png'.format(image_directory))]
static_image_route = '/static/'


@app.server.route('{}<image_path>.png'.format(static_image_route))
def serve_images(image_path):
    print('hello world')
    image_name = f"{image_path}.png"
    if image_name not in list_of_images:
        raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
    return flask.send_from_directory(image_directory, image_name)


@app.callback(
    Output('imagery-carousel', 'items'),
    Output('test-image', 'src'),
    # Input('menu-imagery', 'n_clicks'),
    # Input('test-div', 'loading_state'),
    Input('test-button', 'n_clicks')
)
def display_images(click):
    if click:
        retval1 = [dict(key=str(idx), src=f'{static_image_route}{path}') for idx, path in enumerate(list_of_images)]
        retval2 = static_image_route + list_of_images[0]
        return retval1, retval2

# def get_images():
#     TEST_ASSETS_FOLDER = r"C:\LODAT\test_assets\images"     # note only hard coded this for now
#     images = glob.glob(f"{TEST_ASSETS_FOLDER}\\*.png")
#     return [dict(key=str(idx), src=path) for idx, path in enumerate(images)]



