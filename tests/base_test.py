"""
This script is a base_test script that sets up the initial
configurations of the tests. It creates the flask test
environment in which the tests can run
"""
from flask_testing import TestCase

from instance import environments
from myapp import create_app, db

class BaseTest(TestCase):

    def create_app(self):
        return create_app(environments['testing'])

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()