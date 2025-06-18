from mongoengine import Document, StringField, FloatField, DateTimeField, DictField

class Offer(Document):
    offer_id = StringField(primary_key=True)
    telegram_id = StringField(required=True)
    amount = FloatField(required=True)
    currency = StringField(required=True)
    amount_usd = FloatField(required=True)
    status = StringField(default="open")  # open, funded, completed, cancelled
    details = DictField()
    created_at = DateTimeField()
    meta = {"collection": "offers"}
