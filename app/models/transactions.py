from .db import db, environment, SCHEMA, add_prefix_for_prod


class Transaction(db.Model):
    __tablename__ = 'transactions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    payment_type = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable = False)
    completed = db.Column(db.Boolean, nullable = False)

    #relationships for the sender nd recipient
    sender = db.relationship('User', foreign_keys=[sender_id])
    recipient = db.relationship('User', foreign_keys=[recipient_id])

    def to_dict(self):
        return {
            'id' : self.id,
            'payment_type' : self.payment_type,
            'amount' : self.amount,
            'completed' : self.completed,
            'sender' : self.sender_id,
            'recipient' : self.recipient_id
        }
