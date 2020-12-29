from flask import Flask,render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
#, template_folder='./templates')
app.debug=True
app.config['SECRET_KEY'] = 'jmr'
if app.debug == True:
	toolbar = DebugToolbarExtension(app)

@app.route('/')
def hello_world():
    return render_template('home.html')
    #return 'Hello, World 3!'

@app.route('/bug')
def bug():
    raise
    return render_template('page/home.html')


if __name__ == "__main__":
    app.run( port=8000, host='0.0.0.0')
