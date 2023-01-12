from __init__ import db

class Todos(db.Model):
    """
    Table Name: todos
    Table Info
        - id: user identification
        - data: todo data
    """
    
    __tablename__ = 'todos'
    __table_args__ = { 'mysql_collate': 'utf8_general_ci' }
    
    id = db.Column(db.String(50), primary_key=True, unique=True)
    data = db.Column(db.String(256))
    
    def __init__(self, id, data):
        self.id = id
        self.data = data
        
    def __repr__(self):
        return 'id: %s, data: %s' % (self.id, self.data)
    
    def as_dict(self):
        return { x.name: getattr(self, x.name) for x in self.__table__.columns }