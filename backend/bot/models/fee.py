from mongoengine import Document, StringField, FloatField, DateTimeField

class Fee(Document):
    offer_id = StringField(required=True)
    telegram_id = StringField(required=True)
    value = FloatField(required=True)
    currency = StringField(required=True)
    status = StringField(default="pending")  # pending/paid/refunded
    created_at = DateTimeField()
    meta = {"collection": "fees"}
