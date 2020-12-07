from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from Form import Form
import FormManager
from flask import abort

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')
    
@app.route('/', methods=['POST'])
@app.route('/index.html', methods=['POST'])
def index_post():
    return redirect("/form/"+request.form['search'])
    
@app.route('/form', methods=['POST','GET'])
def createForm():
    if request.method == 'POST':
        form  = Form(
            request.form['form_id'],
            request.form['questions'],
            request.form['block_begin'],
            request.form['block_end'],
            request.form['amount_req'],
            request.form['expiration'],
        )
        FormManager.add(form)
    return render_template('create-form.html')
    
@app.route('/form/<form_id>')
def form(form_id):
    try:
        form = FormManager.get(str(form_id))
        return render_template('form.html', form = form)
    except FileNotFoundError:
        abort(404)
    
@app.route('/form/<form_id>/<tx_id>')
def response(form_id,tx_id):
    form = FormManager.get(form_id)
    response = form.getResponse(tx_id)
    return render_template('response.html', response = response)
    
@app.route('/response')
def submitResponse():
    return render_template('submit-response.html')
@app.route('/response/<form_id>')
def submitResponseWithForm(form_id):
    form = FormManager.get(form_id)
    return render_template('submit-response.html', form = form)
    
    
    
    
