from app.models import db, User, environment, SCHEMA

def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', firstname='John', lastname='Smith')

    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', firstname='Marnie', lastname='Smith')

    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', firstname='Bobbie', lastname='Smith')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.commit()



def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
