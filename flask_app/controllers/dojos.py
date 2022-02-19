from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template('dojos.html', all_dojos=dojos)


@app.route('/dojo/new', methods=['Post'])
def new_dojo():
    data = {
        'name':request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')


@app.route('/dojo/show/<int:id>')
def show(id):
    data ={
        "id": id
    }
    return render_template("show.html", dojo = Dojo.dojo_ninjas(data))


