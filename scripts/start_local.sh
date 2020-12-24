#!/bin/sh 
source $HOME/mysqltuner-flask/bin/activate
cd $HOME/mysqltuner-flask
export FLASK_APP=mysqltuner.py
export FLASK_ENV=development
export FLASK_DEBUG=True
flask run -p8001 -h0.0.0.0    
