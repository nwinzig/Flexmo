from app.models import db, User, environment, SCHEMA, Transaction

def seed_transactions():
    demo_transaction = Transaction(
        sender_id = 1,
        recipient_id = 2,
        payment_type = 'request',
        amount = 30,
        completed = False
    )

    db.session.add(demo_transaction)
    db.session.commit()

def undo_transactions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.transactions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM transactions")

    db.session.commit()
