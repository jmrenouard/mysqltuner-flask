from flask import Flask,render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name='configgalera'
    ramgb=IntegerField('ramgb')
    nbcpu=IntegerField('nbcpu')
    sst_user=StringField('sst_user', validators=[DataRequired()])
    sst_password=StringField('sst_password', validators=[DataRequired()])
    sst_method=StringField('sst_method', validators=[DataRequired()])
    clustername = StringField('clustername', validators=[DataRequired()])
    nbnodes=IntegerField('nbnodes')
    datadir=StringField('datadir', validators=[DataRequired()])

    serverid_1=IntegerField('serverid_1')
    nodename_1=StringField('nodename_1', validators=[DataRequired()])
    ipaddress_1=StringField('ipaddress_1', validators=[DataRequired()])
    
    serverid_2=IntegerField('serverid_2')
    nodename_2=StringField('nodename_2', validators=[DataRequired()])
    ipaddress_2=StringField('ipaddress_2', validators=[DataRequired()])
    
    serverid_3=IntegerField('serverid_3')
    nodename_3=StringField('nodename_3', validators=[DataRequired()])
    ipaddress_3=StringField('ipaddress_3', validators=[DataRequired()])

    serverid_4=IntegerField('serverid_4')
    nodename_4=StringField('nodename_4', validators=[DataRequired()])
    ipaddress_4=StringField('ipaddress_4', validators=[DataRequired()])
    
    serverid_5=IntegerField('serverid_5')
    nodename_5=StringField('nodename_5', validators=[DataRequired()])
    ipaddress_5=StringField('ipaddress_5', validators=[DataRequired()])
    
    serverid_6=IntegerField('serverid_6')
    nodename_6=StringField('nodename_6', validators=[DataRequired()])
    ipaddress_6=StringField('ipaddress_6', validators=[DataRequired()])
    
    serverid_7=IntegerField('serverid_7')
    nodename_7=StringField('nodename_7', validators=[DataRequired()])
    ipaddress_7=StringField('ipaddress_7', validators=[DataRequired()])

app = Flask(__name__)
#, template_folder='./templates')
app.debug=True
app.config['SECRET_KEY'] = 'jmr'
if app.debug == True:
	toolbar = DebugToolbarExtension(app)

@app.route('/')
def hello_world():
    return render_template('home.html',form = MyForm())
    #return 'Hello, World_3!'

@app.route('/bug')
def bug():
    raise
    return render_template('page/home.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

if __name__ == "__main__":
    app.run( port=8000, host='127.0.0.1')
