import copy

import flask
from flask import Flask, render_template, request, redirect, make_response
from random import shuffle
from markupsafe import escape

import Build_model
import main

app = Flask(__name__)

shuffled_build = []
counter = 0
build_amount = 0
slider_values = [0, 0, 0]


# Index
@app.route('/', methods=['GET', 'POST'])
def index():
    global counter
    global shuffled_build
    global build_amount
    global slider_values

    if not shuffled_build:
        shuffled_build = copy.copy(builds)
        shuffle(shuffled_build)
        build_amount = len(shuffled_build)

    if flask.request.method == 'POST':
        item_slider_item_data = request.form.get('item_slider_item', 0)
        item_slider_rune_data = request.form.get('item_slider_rune', 0)
        item_slider_spell_data = request.form.get('item_slider_spell', 0)

        slider_values[0] = int(item_slider_item_data)
        slider_values[1] = int(item_slider_rune_data)
        slider_values[2] = int(item_slider_spell_data)
        print('slider arr = ' + str(slider_values) + ' : item=' + str(slider_values[0]) + ' : runes=' + str(slider_values[1]) + ' : spells=' + str(slider_values[2]))

    if "next" in request.form:
        if counter != build_amount - 1:
            counter += 1
            return redirect(request.referrer)
    elif "fuck go back" in request.form:
        if counter != 0:
            counter -= 1
            return redirect(request.referrer)
    request.form = ""

    cursed_build = main.championBuildVoodoo(slider_values, items, shuffled_build[counter])

    return render_template('home.html', champ_build=cursed_build, lol_items=items, num=counter + 1,
                           num_max=build_amount, slider_arr=slider_values)


@app.route('/list', methods=['GET'])
def champ_list():
    return render_template('list.html', champ_builds=builds, lol_items=items)


@app.route('/items', methods=['GET', 'POST'])
def item_display():
    if flask.request.method == 'POST':
        new_type_list = request.form.getlist('lol-item-typer')
        print(new_type_list)
        i = 0
        for itm in items:
            itm.type = new_type_list[i]
            i += 1
        main.save_object(items, 'lol-items-harvested.plk')

    return render_template('items.html', enum_types=lol_item_type_enums, lol_items=items)


if __name__ == '__main__':
    builds = main.load_object('mobafire-builds.plk')
    items = main.load_object('lol-items-harvested.plk')
    lol_item_type_enums = Build_model.lol_item_type_enums
    app.run()
