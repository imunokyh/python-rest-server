from flask import request
from flask_restx import Api, Resource, Namespace, fields

from models.todos_model import Todos, db

from controllers.auth_check import check_auth

Todo = Namespace(
    name='Todo',
    description='Todo Server API'
)

todo_data = Todo.model('Todo-Data', {
    'data': fields.String(description='a Todo', reqired=True)
})

todo_error = Todo.model('Todo-Error', {
    'message': fields.String(description='message')
})

@Todo.route('/<string:todo_id>')
@Todo.param('todo_id', 'An ID')
class TodoServer(Resource):
    @check_auth
    @Todo.response(200, 'Success', todo_data)
    @Todo.response(401, 'Unauthorized', todo_error)
    @Todo.response(404, 'Not Found', todo_error)
    def get(self, todo_id):
        """todo_id에 해당하는 할 일을 가져온다."""
        try:
            query = Todos.query.filter_by(id=todo_id).first()
            result = { todo_id: query.data }
            status = 200
        except:
            result = { 'message': todo_id + ' is not exist' }
            status = 404
        return result, status
    
    @check_auth
    @Todo.expect(todo_data)
    @Todo.response(200, 'Success', todo_data)
    @Todo.response(401, 'Unauthorized', todo_error)
    @Todo.response(400, 'Invalid Syntax', todo_error)
    def post(self, todo_id):
        """todo_id에 해당하는 할 일을 설정한다."""
        try:
            new_todo = Todos(todo_id, request.json.get('data'))
            db.session.add(new_todo)
            db.session.commit()
            result = { todo_id: new_todo.data }
            status = 200
        except:
            result = { 'message': todo_id + ' put failed' }
            status = 400
        return result, status
    
    @check_auth
    @Todo.expect(todo_data)
    @Todo.response(200, 'Success', todo_data)
    @Todo.response(401, 'Unauthorized', todo_error)
    @Todo.response(400, 'Invalid Syntax', todo_error)
    def put(self, todo_id):
        """todo_id에 해당하는 할 일을 수정한다."""
        try:
            query = Todos.query.filter_by(id=todo_id).first()
            query.data = request.json.get('data')
            db.session.commit()
            result = { todo_id: query.data }
            status = 200
        except:
            result = { 'message': todo_id + ' put failed' }
            status = 400
        return result, status
    
    @check_auth
    @Todo.response(200, 'Success', todo_data)
    @Todo.response(401, 'Unauthorized', todo_error)
    @Todo.response(404, 'Not Found', todo_error)
    def delete(self, todo_id):
        """todo_id에 해당하는 할 일을 삭제한다."""
        try:
            query = Todos.query.filter_by(id=todo_id).first()
            del_data = query.data
            db.session.delete(query)
            db.session.commit()
            result = { todo_id: del_data }
            status = 200
        except:
            result = { 'message': todo_id + ' is not exist' }
            status = 404
        return result, status