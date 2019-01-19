#!flask/bin/python
import os
from controller.models import db, Product
from app import app

with app.app.app_context():
	db.create_all()

	p1 = Product(name="Lavender heart", price=9.25)
	p2 = Product(name="Personalised cufflinks", price=45.00)
	p3 = Product(name="Kids T-shirt", price=19.95)

	db.session.add(p1)
	db.session.add(p2)
	db.session.add(p3)
	db.session.commit()