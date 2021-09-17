import os

import flask
from flask import Flask, render_template, request, redirect, make_response

from ScraperLib import *

app = Flask(__name__)

# Index
@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    legomodel = []
    if os.path.exists ("pickle.rick"):
        legomodel = load_objects_from_path("pickle.rick")

    app.run()