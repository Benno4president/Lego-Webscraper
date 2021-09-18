import os

import flask
from flask import Flask, render_template, request, redirect, make_response

import NumpyAnalyser
from ScraperLib import *

app = Flask(__name__)


# Index
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', models=legomodel)


if __name__ == '__main__':
    legomodel = []
    if os.path.exists("pickle.rick"):
        legomodel = load_objects_from_path("pickle.rick")
    da = NumpyAnalyser.NumpyAnal()

    allprices=[]
    for z in legomodel:
        allprices.append(z.price)


    allitems=[]
    for i in legomodel:
        allitems.append(i.amount_bricks)
    print(da.averagepricepritem(allprices, allitems))



    app.run()


