import jwt
import bcrypt
import time

from flask import request, session
from flask_restx import Resource, Api, Namespace, fields

from models.users_model import Users, db

Auth = Namespace(
    name='Auth',
    description='Auth Server API'
)

auth_user = Auth.model('Auth-User', {
    'id': fields.String(description='User ID', required=True),
    'password': fields.String(description='User Password', required=True)
})

auth_jwt = Auth.model('Auth-JWT', {
    'authorization': fields.String(description='Authorization which you must include in header')
})

auth_error = Auth.model('Auth-Error', {
    'message': fields.String(description='message')
})

@Auth.route('/register')
class AuthRegister(Resource):
    @Auth.expect(auth_user)
    @Auth.response(200, 'Success', auth_jwt)
    @Auth.response(500, 'Internal Server Error', auth_error)
    def post(self):
        """사용자 등록"""
        id = request.json.get('id')
        pwd = request.json.get('password')
        query = Users.query.filter_by(id=id).first()
        if query != None:
            result = { 'message': id + ' already exist'}
            status = 500
        else:
            now = time.time()
            new_user = Users(id, bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt()), jwt.encode({'id': id, 'time': str(now)}, 'secret', algorithm='HS256').decode('utf-8'))
            db.session.add(new_user)
            db.session.commit()
            result = { 'authorization': jwt.encode({'id': id, 'time': now}, 'secret', algorithm='HS256').decode('utf-8') }
            status = 200
        return result, status
    
    @Auth.expect(auth_user)
    @Auth.response(200, 'Sucess')
    @Auth.response(404, 'Not Found', auth_error)
    @Auth.response(500, 'Internal Server Error', auth_error)
    def delete(self):
        """사용자 해지"""
        id = request.json.get('id')
        pwd = request.json.get('password')
        query = Users.query.filter_by(id=id).first()
        if query == None:
            result = { 'message': user_id + ' not exist' }
            status = 404
        elif not bcrypt.checkpw(pwd.encode('utf-8'), query.password.encode('utf-8')):
            result = { 'message': 'password wrong' }
            status = 500
        else:
            result = {}
            del_user = query
            db.session.delete(del_user)
            db.session.commit()
            if id in session:
                session.pop(id, None)
            status = 200
        return result, status
    
@Auth.route('/login')
class AuthLogin(Resource):
    @Auth.expect(auth_user)
    @Auth.response(200, 'Success', auth_jwt)
    @Auth.response(403, 'Forbidden', auth_error)
    @Auth.response(404, 'Not Found', auth_error)
    @Auth.response(500, 'Internal Server Error', auth_error)
    def post(self):
        """사용자 로그인"""
        id = request.json.get('id')
        pwd = request.json.get('password')
        query = Users.query.filter_by(id=id).first()
        if query == None:
            result = { 'message': id + ' not found'}
            status = 404
        elif not bcrypt.checkpw(pwd.encode('utf-8'), query.password.encode('utf-8')):
            result = { 'message': 'password wrong' }
            status = 500
        elif id in session:
            result = { 'message': id + ' already login' }
            status = 403
        else:
            session[id] = id
            now = time.time()
            query.token = jwt.encode({'id': id, 'time': now}, 'secret', algorithm='HS256').decode('utf-8')
            db.session.commit()
            result = { 'authorization': jwt.encode({'id': id, 'time': now}, 'secret', algorithm='HS256').decode('utf-8') }
            status = 200
        return result, status
    
@Auth.route('/logout')
class AuthLogout(Resource):
    @Auth.expect(auth_user)
    @Auth.response(200, 'Success', auth_error)
    @Auth.response(204, 'No Content', auth_error)
    def delete(self):
        """사용자 로그아웃"""
        id = request.json.get('id')
        if id not in session:
            result = { 'message': id + ' already logout' }
            status = 204
        else:
            result = { 'message': id + ' logout' }
            session.pop(id, None)
            status = 200
        return result, status