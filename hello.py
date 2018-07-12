from flask import Flask,redirect, url_for, request, render_template, flash
from wtforms import form
app = Flask(__name__)

 
@app.route('/home')
def home():		

	return render_template('index.html')

@app.route('/ingreso', methods=['GET', 'POST'])
def ingreso():
	if request.method=='POST':
		if request.form['submit']=='subir':
			return redirect(url_for('index'))
	elif request.method=='GET':
		return render_template('ingreso_cliente.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('ingreso'))

    # show the form, it wasn't submitted
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True)