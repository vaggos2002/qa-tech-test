from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    price = db.Column(db.Float())

    @property
    def serialize(self):
    	return { 
    		'id' : self.id,
    		'name' : self.name,
    		'price' : '%.2f' % self.price 
    	}
