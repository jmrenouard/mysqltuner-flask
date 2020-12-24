#!/bin/sh
source $HOME/mysqltuner-flask/bin/activate
cd $HOME/mysqltuner-flask
export FLASK_APP=mysqltuner.py
export FLASK_ENV=development
export FLASK_DEBUG=True
flask run -p8001 -hmysqltuner.lightpath.fr \
--cert /etc/nginx/ssl/mysqltuner.lightpath.fr.crt  \
--key /etc/nginx/ssl/mysqltuner.lightpath.fr.key
