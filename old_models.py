# coding: utf-8
from sqlalchemy import CHAR, Column, Float, ForeignKey, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER, SMALLINT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(INTEGER(11), primary_key=True)
    brand_name = Column(String(100))
    image = Column(String(244))


class ContractProvider(Base):
    __tablename__ = 'contract_providers'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(244))
    sam_id = Column(String(45))
    vat_code = Column(String(45))
    erp_id = Column(String(45))
    crm_id = Column(String(45))
    locale = Column(String(45))
    slug = Column(String(250), nullable=False)
    created = Column(TIMESTAMP)
    modified = Column(TIMESTAMP)


class Fueltype(Base):
    __tablename__ = 'fueltypes'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(100))


class Segment(Base):
    __tablename__ = 'segments'

    id = Column(INTEGER(11), primary_key=True)
    label = Column(CHAR(3))
    description = Column(String(45))


class Car(Base):
    __tablename__ = 'cars'

    id = Column(INTEGER(11), primary_key=True)
    brand_id = Column(INTEGER(11), nullable=False, index=True)
    fueltype_id = Column(INTEGER(11), nullable=False, index=True)
    model = Column(String(100), nullable=False)
    segment_id = Column(ForeignKey('segments.id'), nullable=False, index=True)
    image = Column(Text)

    segment = relationship('Segment')


class TemplateCollection(Base):
    __tablename__ = 'template_collections'

    id = Column(INTEGER(11), primary_key=True)
    collectionname = Column(String(45))
    description = Column(String(244))
    providername = Column(String(244))
    provider_id = Column(ForeignKey('contract_providers.id', ondelete='SET NULL'), index=True)
    slug = Column(String(255), nullable=False, unique=True)
    created = Column(TIMESTAMP)
    modified = Column(TIMESTAMP)

    provider = relationship('ContractProvider')


class User(Base):
    __tablename__ = 'users'

    id = Column(INTEGER(11), primary_key=True)
    username = Column(String(45))
    password = Column(String(244))
    is_active = Column(SMALLINT(6), server_default=text("'1'"))
    is_verified = Column(SMALLINT(6), server_default=text("'0'"))
    is_blocked = Column(SMALLINT(6), server_default=text("'0'"))
    is_super_user = Column(SMALLINT(6), server_default=text("'0'"))
    is_provider = Column(INTEGER(11), nullable=False)
    created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    modified = Column(TIMESTAMP)
    email = Column(String(255), nullable=False)
    provider_id = Column(ForeignKey('contract_providers.id'), index=True)

    provider = relationship('ContractProvider')


class Template(Base):
    __tablename__ = 'template'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(45))
    description = Column(String(45))
    details = Column(String(45))
    age_min = Column(INTEGER(11))
    age_max = Column(INTEGER(11))
    template_collection_id = Column(ForeignKey('template_collections.id', ondelete='SET NULL'), index=True)
    template_logo = Column(Text)
    template_type = Column(INTEGER(11), server_default=text("'100'"))
    filters = Column(Text)
    created = Column(TIMESTAMP)
    modified = Column(TIMESTAMP)
    slug = Column(String(244), nullable=False, unique=True)
    hourly_rate = Column(Float(8, True))

    template_collection = relationship('TemplateCollection')


class UserToken(Base):
    __tablename__ = 'user_tokens'

    token = Column(String(255), nullable=False)
    created = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    is_active = Column(TINYINT(255), nullable=False, server_default=text("'1'"))
    user_id = Column(ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    id = Column(INTEGER(255), primary_key=True)
    data = Column(String(255), nullable=False)
    type = Column(TINYINT(255), nullable=False, server_default=text("'1'"))
    expire_date_time = Column(TIMESTAMP)

    user = relationship('User')


class TemplateFilter(Base):
    __tablename__ = 'template_filters'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(INTEGER(11))
    template_id = Column(ForeignKey('template.id', ondelete='CASCADE'), index=True)
    type = Column(TINYINT(4))

    template = relationship('Template')


class TemplatePriceConfig(Base):
    __tablename__ = 'template_price_config'

    id = Column(INTEGER(11), primary_key=True)
    segment_id = Column(ForeignKey('segments.id', ondelete='SET NULL'), index=True)
    mileageinterval = Column(INTEGER(11))
    timeinterval = Column(INTEGER(11))
    price = Column(Float(8, True))
    template_id = Column(ForeignKey('template.id', ondelete='CASCADE'), nullable=False, index=True)
    fueltype_id = Column(ForeignKey('fueltypes.id', ondelete='SET NULL'), index=True)
    created = Column(TIMESTAMP)
    modified = Column(TIMESTAMP)
    slug = Column(String(244), nullable=False, unique=True)
    duration_interval = Column(INTEGER(11), server_default=text("'12'"))
    repair_ratio = Column(Float(8, True))
    car_id = Column(ForeignKey('cars.id', ondelete='CASCADE'), index=True)

    car = relationship('Car')
    fueltype = relationship('Fueltype')
    segment = relationship('Segment')
    template = relationship('Template')


class TemplateRepairConfig(Base):
    __tablename__ = 'template_repair_config'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    repair_time_minutes = Column(INTEGER(11))
    parts_cost = Column(Float(12))
    km_interval = Column(INTEGER(11))
    duration_interval_months = Column(INTEGER(11))
    created = Column(TIMESTAMP)
    modified = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    template_price_config_id = Column(ForeignKey('template_price_config.id', ondelete='CASCADE'), index=True)
    slug = Column(String(150), nullable=False, unique=True)
    hourly_rate = Column(Float(8, True))

    template_price_config = relationship('TemplatePriceConfig')
