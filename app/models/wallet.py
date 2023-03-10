from .db import db, environment, SCHEMA, add_prefix_for_prod



class Wallet(db.Model):
    __tablename__ = 'wallets'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    funds = db.Column(db.Float, default = 0)
