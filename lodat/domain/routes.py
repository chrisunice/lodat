from flask import render_template
from lodat.domain.crawler import crawler


def home():
    return render_template('index.html')


def send_images():
    images = crawler('../../reference/images/')
    return ';'.join(images)
