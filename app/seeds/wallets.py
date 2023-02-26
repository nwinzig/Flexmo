from app.models import db, Wallet, environment, SCHEMA

def seed_wallets():
    demo_wallet = Wallet(
        user = demo
    )

    db.session.add(demo_wallet)
    db.session.commit()


def undo_wallets():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM wallets")

    db.session.commit()
