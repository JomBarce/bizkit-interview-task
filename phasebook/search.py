from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    filtered_users = []

    # Check if search parameter is empty
    if not args:
        filtered_users = USERS

    # Filter the users according to the search parameter priority
    if 'id' in args:
        filtered_users += [user for user in USERS if args['id'] == user['id']]

    if 'name' in args:
        filtered_users += [user for user in USERS if args['name'].lower() in user['name'].lower()]

    if 'age' in args:
        try:
            age = int(args['age'])
            filtered_users += [user for user in USERS if user['age'] in (age - 1, age, age + 1)]
        except ValueError:
            pass

    if 'occupation' in args:
        filtered_users += [user for user in USERS if args['occupation'].lower() in user['occupation'].lower()]

    # Remove duplicate users using dictionary
    unique_users_dict = {}
    for user in filtered_users:
        unique_users_dict[user['id']] = user

    # Convert back to list
    unique_users = list(unique_users_dict.values())

    return unique_users