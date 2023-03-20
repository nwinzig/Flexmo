from app.models import db, User, environment, SCHEMA, Transaction

def seed_transactions():
    demo_transaction = Transaction(
        sender_id = 1,
        recipient_id = 2,
        payment_type = 'request',
        amount = 30,
        completed = False
    )
    demo_transaction2 = Transaction(
        sender_id = 1,
        recipient_id = 3,
        payment_type = 'pay',
        amount = 13.45,
        completed = True
    )
    demo_transaction3 = Transaction(
        sender_id = 2,
        recipient_id = 1,
        payment_type = 'request',
        amount = 45.60,
        completed = True
    )
    demo_transaction4 = Transaction(
        sender_id = 3,
        recipient_id = 2,
        payment_type = 'request',
        amount = 16.22,
        completed = False
    )
    db.session.add(demo_transaction)
    db.session.add(demo_transaction2)
    db.session.add(demo_transaction3)
    db.session.add(demo_transaction4)
    db.session.commit()

def undo_transactions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.transactions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM transactions")

    db.session.commit()
