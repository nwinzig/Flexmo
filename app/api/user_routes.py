from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
# @login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
# @login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)

    # user = User.query.get(id).join(User.wallet)
    return user.to_dict()

# route to allow user to add funds to their wallet
# @user_routes.route('/<int:id>/wallet/add', methods=['PUT'])
    # find user
    # use wallet form to recieve user info and new fund info
    # adjust user current balance based on incoming data
    # save database with new user funds
    # return user

#route to allow user to remove funds from their wallet
