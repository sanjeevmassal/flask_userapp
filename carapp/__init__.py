from flask import Blueprint
from .models import Car, Brand
from .admin import CarAdmin, BrandAdmin
carapp = Blueprint('cars',__name__,template_folder='templates')
from app.extensions import admin_panel, db
admin_panel.add_view(CarAdmin(Car, db.session))
admin_panel.add_view(BrandAdmin(Brand, db.session))