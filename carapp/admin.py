from flask_admin.contrib.sqla import ModelView

class CarAdmin(ModelView):
    form_excluded_columns = ['slug', 'created','updated','car_variants']

class BrandAdmin(ModelView):
    form_excluded_columns = ['slug', 'created','updated','cars']
