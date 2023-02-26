from app.models import db, User, environment, SCHEMA, Wallet


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', firstname='John', lastname='Smith')

    demo_wallet = Wallet(
        user = demo
    )

    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', firstname='Marnie', lastname='Smith')

    marnie_wallet = Wallet(
        user = marnie
    )

    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', firstname='Bobbie', lastname='Smith')

    bobbie_wallet = Wallet(
        user = bobbie
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(demo_wallet)
    db.session.add(marnie_wallet)
    db.session.add(bobbie_wallet)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        db.session.execute("DELETE FROM wallets")

    db.session.commit()
