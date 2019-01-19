import connexion
from controller.models import db


import logging
for l in ['connexion.api', 'connexion.decorators.decorator',
		  'connexion.decorators.response',
		  'connexion.api.security',
		  'connexion.decorators.produces',
		  'connexion.resolver',
		  'connexion.decorators.validation','connexion.app']:
	root = logging.getLogger(l)
	if root.handlers:
	    for handler in root.handlers:
	        root.removeHandler(handler)
	logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

app = connexion.App(__name__, specification_dir='swagger/',debug=True)
app.add_api('python-tech-test.yaml')
app.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

db.init_app(app.app)

if __name__ == "__main__":
	app.run()

