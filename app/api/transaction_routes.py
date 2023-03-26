from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, db, Transaction
from sqlalchemy import or_

transaction_routes = Blueprint('transactions', __name__)

@transaction_routes.route('/all')
# @login_required
def get_all_transactions():
    """get all transactions from the database """

    transactions = Transaction.query.all()

    return {'transactions': [transaction.to_dict() for transaction in transactions]}


@transaction_routes.route('/<int:id>')
# @login_required
def get_one_transaction(id):
    """get one transaction by transaction id """

    transaction = Transaction.query.get(id)

    return {'transaction': transaction.to_dict()}


@transaction_routes.route('/my/<int:id>')
# @login_required
def get_user_transactions(id):
    """get all transactions associated with the user """

    transactions = Transaction.query.filter(or_(Transaction.sender_id == id,Transaction.recipient_id == id)).all()

    return {'transactions': [transaction.to_dict() for transaction in transactions]}


# create a transaction



# complete a currently pending transaction
