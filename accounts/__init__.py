from flask import Blueprint
account = Blueprint('accounts',__name__, template_folder='templates')
from . import views

