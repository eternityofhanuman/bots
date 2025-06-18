from mongoengine import Document, StringField, DateTimeField

class SupportTicket(Document):
    telegram_id = StringField(required=True)
    question = StringField()
    status = StringField(default="open")  # open, resolved, escalated
    created_at = DateTimeField()
    meta = {"collection": "support_tickets"}
