"""
Script contains the model for a bucketlist items
"""
from myapp import db
from datetime import datetime
import pytz

class BucketListItem(db.Model):
    """
    Class used as a representation of the bucketlist item model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, nullable=False)
    created = db.Column(
        db.DateTime,
        default=datetime.now(tz=pytz.timezone('Africa/Kampala'))
    )
    modified = db.Column(
        db.DateTime,
        default=datetime.now(tz=pytz.timezone('Africa/Kampala')),
        onupdate=datetime.now(tz=pytz.timezone('Africa/Kampala'))
    )
    expiry = db.Column(
        db.DateTime,
        nullable=False
    )
    bucketlist_id = db.Column(db.Integer, db.ForeignKey('bucketlist.id'), nullable=False)
    