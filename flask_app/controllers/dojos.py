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























# @app.route("/")
# def index():
#     return render_template("dojos.html", all_dojos = Dojo.get_all())


# @app.route('/dojos/create', methods=['Post'])
# def dojos_create():
#     # Dojo.create_dojo(request.form)  ->update this
#     return redirect ('/')


# # new user page
# @app.route('/create_user')
# def create_user():
#     return render_template('create.html')



# # edit display page
# @app.route('/user_update/<int:id>')
# def user_updated(id):
#     data = {
#         "id": id
#     }
#     return render_template('update.html', user = Users.single_user(data))


# @app.route('/update_complete', methods=['POST'])
# def update_complete():
#     Users.update_user(request.form)
#     return redirect ('/')



# # delete
# @app.route('/delete_user/<int:id>')
# def delete_user(id):
#     data = {
#         "id":id
#     }
#     Users.delete_user(data)
#     return redirect ('/') 



# @app.route('/show_user/<int:id>')
# def show(id):
#     data ={
#         "id":id
#     }
#     return render_template("show.html", user = Users.single_user(data))