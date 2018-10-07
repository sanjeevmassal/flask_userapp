from app.extensions import db
from app.core.models import TimestampSlugMixin, SlugModelMixin
from app.core.string import slugify

class Brand(db.Model, TimestampSlugMixin):
    __tablename__ = 'brands'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(244))
    cars = db.relationship('Car', backref="brand", cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, *args, **kwargs):
        import pdb
        pdb.set_trace()
        if not 'slug' in kwargs or kwargs.get('slug', '')=='':
            self.slug = slugify(self.name)
        super(Brand, self).__init__(*args, **kwargs)

class Fuel(db.Model,SlugModelMixin):
    __tablename__ = 'fuels'

    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(100))
    cars = db.relationship('CarVariant', backref="fuel", cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs or kwargs.get('slug','')=='':
            self.slug = slugify(self.name)
        super(Fuel, self).__init__(*args, **kwargs)

class Segment(db.Model,TimestampSlugMixin):
    __tablename__ = 'segments'

    id = db.Column(db.INTEGER, primary_key=True)
    label =db. Column(db.CHAR(3))
    description = db.Column(db.String(45))
    cars = db.relationship('Car', backref="segment", cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs or kwargs.get('slug','')=='':
            self.slug = slugify(self.label)
        super(Segment, self).__init__(*args, **kwargs)

class Car(db.Model,TimestampSlugMixin):
    __tablename__ = 'cars'

    id = db.Column(db.INTEGER, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'),nullable=False, index=True)
    model = db.Column(db.String(100), nullable=False)
    segment_id = db.Column(db.ForeignKey('segments.id'), nullable=False, index=True)
    image = db.Column(db.Text)
    car_variants = db.relationship('CarVariant', backref="car", cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs or kwargs.get('slug', '') == '':
            brand = Brand.query.get(id=self.brand_id)
            if brand:
                self.slug = slugify('%s %s' % (brand.name,self.model))
            else:
                self.slug = slugify(self.model)
        super(Car, self).__init__(*args, **kwargs)

class CarVariant(db.Model, TimestampSlugMixin):
    __tablename__ = 'car_variants'
    id = db.Column(db.INTEGER, primary_key=True)
    fuel_id = db.Column(db.Integer, db.ForeignKey('fuels.id'), nullable=False, index=True)
    car_id = db.Column(db.Integer,db.ForeignKey('cars.id'), nullable=False, index=True)
    variant = db.Column(db.String(244),nullable=True)

    def __init__(self, *args, **kwargs):
        if not 'slug' in kwargs or kwargs.get('slug', '') == '':
            car = Car.query.get(id=self.car_id)
            fuel = Car.query.get(id=self.fuel_id)
            if car:
                self.slug = slugify('%s %s %s' % (car.slug,self.variant,fuel.slug))
            else:
                self.slug = slugify(self.model)
        super(CarVariant, self).__init__(*args, **kwargs)