#!/usr/bin/python
from app import app

app.secret_key = 'dev'  # change this before making app public
app.config['SESSION_TYPE'] = 'filesystem'

app.run("0.0.0.0", port=8080, debug=True)
