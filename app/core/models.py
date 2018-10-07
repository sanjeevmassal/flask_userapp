from datetime import datetime
from ..extensions import db


class SlugModelMixin(object):
    slug = db.Column(db.String(244))


class TimestampMixin(object):
    created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)

class TimestampSlugMixin(SlugModelMixin,TimestampMixin):
    pass
