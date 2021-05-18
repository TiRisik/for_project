from flask import Flask, request, render_template, redirect, url_for
from mongodb_class import User, Date, Person
from mongoengine import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
connect('db', host='mongodb+srv://Tiris:Et21121982@anibus.rzt5y.mongodb.net/db?retryWrites=true&w=majority')
result_user = None


@app.route('/login', methods=['GET', 'POST'])
def login():
    global result_user
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result_user = list(User.objects(log_user=email))
        if result_user:
            if password == result_user[0].pass_user:
                return render_template('main.html')
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')


@app.route("/main")
def main():
    return render_template('main.html')


@app.route("/information", methods=['GET', 'POST'])
def informaon():
    if request.method == 'GET':
        return render_template('secret_two.html')
    elif request.method == 'POST':
        date1 = request.form['date']
        result_date = list(Date.objects(date=date1))
        return render_template('secret_two.html', tovar=result_date[0].data)


@app.route("/people",  methods=['GET', 'POST'])
def information():
    if request.method == 'GET':
        result_person = list(Person.objects(search=1))
        h = []
        for i in result_person:
            fio = i.name + ' ' + i.surname + ' ' + i.otchestvo
            h.append([fio, i.age, i.dolgnost])
        return render_template('secret_three.html', tovar=h)
    elif request.method == 'POST':
        if request.form['button'] == 'plus':
            return redirect(url_for('secret'))
        else:
            return redirect(url_for('secret_four'))


@app.route("/secret", methods=['GET', 'POST'])
def secret():
    if request.method == 'GET':
        return render_template('secret.html')
    elif request.method == 'POST':
        f = request.files['file']
        sfname = 'static/img/a.jpg'
        f.save(sfname)
        new_person = Person(name=request.form['name'], surname=request.form['name2'], otchestvo=request.form['name3'],\
                            age=request.form['age'], search=1, dolgnost=request.form['dolgnost'], photo='static/img/a.jpg').save()
        return redirect(url_for('main'))


@app.route("/secret_four", methods=['GET', 'POST'])
def secret_four():
    if request.method == 'GET':
        return render_template('secret_four.html')
    elif request.method == 'POST':
        results = list(Person.objects(surname=request.form['name2']))
        for i in results:
            if i.name == request.form['name'] and i.otchestvo == request.form['name3']:
                i.delete()
        return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
