from __init__ import create_app, db

from flask_restx import Api

from apis.echo import Echo
from apis.todo import Todo
from apis.auth import Auth

authrizations = {
    'API Key': {
        'type': 'apiKey',
        'name': 'authorization',
        'in': 'header'
    }
}

app = create_app()
api = Api(
    app,
    version='0.0.1',
    title='Yunho\'s REST API Server',
    description='Yunho\'s REST API Test Server',
    authorizations=authrizations,
    security='API Key'
)

api.add_namespace(Auth, '/auth')
api.add_namespace(Echo, '/echo')
api.add_namespace(Todo, '/todo')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)