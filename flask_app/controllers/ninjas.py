from flask import render_template, request, redirect
from flask_app import app
from flask_app.controllers.dojos import dojos
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/ninjas')
def ninjas():
    return render_template("ninja.html", dojos = Dojo.get_all())


@app.route('/ninja/create', methods=['Post'])
def new_ninja():
    Ninja.create_ninjas(request.form)
    return redirect('/dojos')


