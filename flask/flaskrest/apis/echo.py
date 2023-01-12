from flask import request
from flask_restx import Api, Resource, Namespace, fields

Echo = Namespace(
    name='Echo',
    description='Echo Server API'
)

echo_data = Echo.model('Echo-Data', {
    'any data 1': fields.String(description='any string data'),
    'any data 2': fields.Integer(description='any integer data'),
    'any data 3': fields.Float(description='any float data')
})

echo_nobody = Echo.model('Echo-Nobody', {
    'uri': fields.String(description='request uri'),
    'method': fields.String(description='request method'),
    'header': fields.String(description='request header')
})

echo_body = Echo.inherit('Echo-Body', echo_nobody, {
    'body': fields.String(description='request body')
})

@Echo.route('')
class EchoServer(Resource):
    @Echo.response(200, 'Success', echo_nobody)
    def get(self):
        """GET METHOD에 대한 Echo 기능을 수행합니다."""
        result = { 
            'uri': request.url,
            'method': request.method,
            'header': dict(request.headers)
        }
        return result, 200
        
    @Echo.expect(echo_data)
    @Echo.response(200, 'Success', echo_body)
    def post(self):
        """POST METHOD에 대한 Echo 기능을 수행합니다."""
        result = { 
            'uri': request.url,
            'method': request.method,
            'header': dict(request.headers),
            'body': request.get_json()
        }
        return result, 200
    
    @Echo.expect(echo_data)
    @Echo.response(200, 'Success', echo_body)
    def put(self):
        """PUT METHOD에 대한 Echo 기능을 수행합니다."""
        result = {
            'uri': request.url,
            'method': request.method,
            'header': dict(request.headers),
            'body': request.get_json()
        }
        return result, 200
    
    @Echo.response(200, 'Success', echo_nobody)
    def delete(self):
        """DELETE METHOD에 대한 Echo 기능을 수행합니다."""
        result = {
            'uri': request.url,
            'method': request.method,
            'header': dict(request.headers)
        }
        return result, 200