from flask import Flask,render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,RadioField,SelectField
from wtforms.validators import DataRequired,IPAddress

class MyForm(FlaskForm):
    name='configGalera'
    ramgb=IntegerField( id='ramgb', default=2)
    nbcpu=IntegerField( id='nbcpu',default=2)
    datadir=StringField( id='datadir', validators=[DataRequired()], default='/var/lib/mysql')
    sst_user=StringField( id='sst_user', validators=[DataRequired()], default="sst_user")
    sst_password=StringField( id='sst_password', validators=[DataRequired()], default="sst_password")
    sst_method=SelectField( id='sst_method', validators=[DataRequired()], choices=[('mariabackup', 'MariaDB Backup'), ('rsync', 'Rsync'), ('clone', 'Clone'), ('mysqldump', 'MySQL Dump')])
    clustername = StringField( id='clustername', validators=[DataRequired()], default='MyCluster')
    nbnodes=RadioField( id='nbnodes', choices=[(3, '3 nodes'), (5, '5 nodes'), (7, '7 nodes')], default=3)

    serverid_1=IntegerField(id='serverid_1', label="1st server id", default=1)
    nodename_1=StringField( id='nodename_1', validators=[DataRequired()], default='server1')
    ipaddress_1=StringField( id='ipaddress_1', validators=[DataRequired()])
    
    serverid_2=IntegerField( id='serverid_2', default=2)
    nodename_2=StringField( id='nodename_2', validators=[DataRequired()], default='server2')
    ipaddress_2=StringField( id='ipaddress_2', validators=[IPAddress(ipv4=True)])
    
    serverid_3=IntegerField( id='id_3', default=3)
    nodename_3=StringField( id='name_3', validators=[DataRequired()], default='server3')
    ipaddress_3=StringField( id='address_3', validators=[IPAddress(ipv4=True)])

    serverid_4=IntegerField( id='id_4', default=4)
    nodename_4=StringField( id='name_4', validators=[DataRequired()], default='server4')
    ipaddress_4=StringField( id='address_4', validators=[IPAddress(ipv4=True)])
    
    serverid_5=IntegerField( id='id_5', default=5)
    nodename_5=StringField( id='name_5', validators=[DataRequired()], default='server5')
    ipaddress_5=StringField( id='address_5', validators=[IPAddress(ipv4=True)])
    
    serverid_6=IntegerField( id='id_6', default=6)
    nodename_6=StringField( id='name_6', validators=[DataRequired()], default='server6')
    ipaddress_6=StringField( id='address_6', validators=[IPAddress(ipv4=True)])
    
    serverid_7=IntegerField( id='id_7', default=7)
    nodename_7=StringField( id='name_7', validators=[DataRequired()], default='server7')
    ipaddress_7=StringField( id='address_7', validators=[IPAddress(ipv4=True)])

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
