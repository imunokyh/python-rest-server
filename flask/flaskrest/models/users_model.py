from __init__ import db

class Users(db.Model):
    """
    Table Name: users
    Table Info
        - id: user identification
        - password: user password
        - token: user json web token
    """
    
    __tablename__ = 'users'
    __table_args__ = { 'mysql_collate': 'utf8_general_ci' }
    
    id = db.Column(db.String(50), primary_key=True, unique=True)
    password = db.Column(db.String(256))
    token = db.Column(db.String(256))
    
    def __init__(self, id, password, token):
        self.id = id
        self.password = password
        self.token = token
        
    def __repr__(self):
        return 'id: %s, password: %s, token: %s' % (self.id, self.password, self.token)
    
    def as_dict(self):
        return { x.name: getattr(self, x.name) for x in self.__table__.columns }