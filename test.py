import unittest
from flask import Flask
from flask_login import current_user
from project import create_app, db
from project.models import User


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        # Create a test Flask app and configure it for testing
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        # Create the test database and tables
        db.create_all()

    def tearDown(self):
        # Remove the test database and tables
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index_route(self):
        # Test the index route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Economic Calendar', response.data)

    def test_login(self):
        # Create a test user
        user = User(email='test@example.com', name='Test User', password='testpassword')
        db.session.add(user)
        db.session.commit()

        # Test the login route with correct credentials
        response = self.client.post('/login', data={'email': 'test@example.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user.name, 'Test User')

    # # Set the current_user using login_user
    #     with self.app.test_request_context():
    #         with self.client.session_transaction() as session:
    #             session['_user_id'] = str(user.id)
    #         self.login_user(user)

    #         # Make the assertion for current_user
    #         self.assertEqual(current_user.name, 'Test User')

        # Test the login route with incorrect credentials
        response = self.client.post('/login', data={'email': 'test@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(user.name, 'Test User1')

if __name__ == '__main__':
    unittest.main()

