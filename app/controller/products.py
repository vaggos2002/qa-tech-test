from flask import request

import sys,os
sys.path.append(os.path.dirname(__file__))

from models import Product, db

def products_list():
	return [ p.serialize for p in Product.query.all() ]

def create_product():
	name = request.form['name']
	price = request.form['price']

	product = Product(name=name,price=price)
	db.session.add(product)
	db.session.commit()

def get_product(product_code):
	product = Product.query.get_or_404(product_code)
	return product.serialize

def update_product(product_code):
	product = Product.query.get_or_404(product_code)

	if 'name' in request.form:
		product.name = request.form['name']
	if 'price' in request.form:
		product.price = request.form['price']

	db.session.commit()

def delete_product(product_code):
	product = Product.query.get_or_404(product_code)
	db.session.delete(product)
	db.session.commit()
