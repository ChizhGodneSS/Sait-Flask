from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client.db'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(main)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    surname = db.Column(db.String(200), nullable=False)
    mail = db.Column(db.String(300), nullable=False)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/contacts', methods=['POST', 'GET'])
def contacts():
    if request.method == "POST":
        name = request.form['name']
        surname = request.form['surname']
        mail = request.form['mail']

        client = Client(name=name, surname=surname, mail=mail)

        try:
            db.session.add(client)
            db.session.commit()
            return redirect('/contacts')
        except:
            return "Ошибка"
    else:
        return render_template('/contacts.html')


@main.route('/services')
def services():
    return render_template('/services.html')


@main.route('/achiev')
def achiev():
    return render_template('achiev.html')


if __name__ == "__main__":
    main.run(debug=True)


