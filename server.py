from flask import Flask, render_template, url_for, request


app = Flask(__name__,template_folder='templates')


@app.route('/')
def home_slash():
    return render_template('index.html')


@app.route('/index.html')
def home_index():
    return render_template('index.html')


@app.route('/generic.html')
def generic():
    return render_template('generic.html')


@app.route('/elements.html')
def elements():
    return render_template('elements.html')


#Esta app permitía la generación automática de links, pero no me dejaba tener página de error 404.
#@app.route('/<string:page_name>')
#def page_name(page_name):
#    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return 'se ha enviado la información'
    else:
        return 'nothing submitted'


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")