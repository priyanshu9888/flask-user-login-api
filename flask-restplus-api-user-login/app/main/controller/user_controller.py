from flask import jsonify, request
from flask_restx import Resource,reqparse

from app.main.util.dto import UserDto
# from app. main.service.user_service import save_new_user, get_all_users, get_a_user
# from typing import Dict, Tuple

api = UserDto.api
# _user = UserDto.user


# @api.route('/')
# class UserList(Resource):
#     @api.doc('list_of_registered_users')
#     @api.marshal_list_with(_user, envelope='data')
#     def get(self):
#         """List all registered users"""
#         return get_all_users()

#     @api.expect(_user, validate=True)
#     @api.response(201, 'User successfully created.')
#     @api.doc('create a new user')
    
#     def post(self) -> Tuple[Dict[str, str], int]:
#         """Creates a new User """
#         data = request.json
#         return save_new_user(data=data)


# @api.route('/public_id')
# @api.param('public_id', 'The User identifier')
# # @api.param('email', 'The User identifier')
# @api.response(404, 'User not found.')
# class User(Resource):
#     @api.doc('get a user')
#     @api.marshal_with(_user)
#     def get(self, public_id):
#         """get a user given its identifier"""
#         print(public_id)
#         user = get_a_user(public_id)
#         if not user:
#             api.abort(404)
#         else:
#             return user

@api.route('/user')



class getuser(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name',action="append" ,help="Name cannot be blank!")
        parser.add_argument('email',action="append")

        args = parser.parse_args()
        return args