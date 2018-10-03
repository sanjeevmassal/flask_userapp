import os
from flask import Flask

from flask import render_template
from app.extensions import db, login_manager
from app.conf import app_config

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('layouts/base.html')

if __name__ == '__main__':
    print(os.environ)
    print('----------')
    app.config.from_object(app_config[os.environ['CONFIG_NAME']])
    db.init_app(app)
    login_manager.init_app(app)
    app.run(debug=True)