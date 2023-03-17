from app.models import db, User, environment, SCHEMA, Transaction

def seed_transactions():
    demo_transaction = Transaction(
        type = 'request',
        amount = 30,
        completed = False
    )
