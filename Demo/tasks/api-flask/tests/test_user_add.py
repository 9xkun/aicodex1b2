import unittest
from app import create_app
from flask_sqlalchemy import SQLAlchemy
import tempfile
import os
from app.database import db

# test_user_controller.py

class TestUserAdd(unittest.TestCase):
    def setUp(self):
        # python server
        # Create a temporary database for testing
        config = {
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'TESTING': True
        }
        self.app = create_app(config=config)

        # python browser
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_user_valid(self):
        response = self.client.post('/api/users', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'age': 25,
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_create_user_missing_email(self):
        response = self.client.post('/api/users', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'phone': '1234567890',
            'age': 25,
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Email is required', response.get_json()['message'])

    def test_create_user_invalid_email(self):
        response = self.client.post('/api/users', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'invalid-email',
            'phone': '1234567890',
            'age': 25,
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email format', response.get_json()['message'])

    def test_create_user_invalid_phone(self):
        response = self.client.post('/api/users', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '123456789',
            'age': 25,
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Phone should be 10 digits', response.get_json()['message'])

    def test_create_user_invalid_age(self):
        response = self.client.post('/api/users', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'age': 150,
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Age should be between 0 and 100', response.get_json()['message'])

    def test_create_user_short_password(self):
        response = self.client.post('/api/users', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe@example.com',
            'phone': '1234567890',
            'age': 25,
            'password': '123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password should be at least 6 characters', response.get_json()['message'])

        def test_create_user_sqlite_connection_error(self):
            # Simulate a database connection error
            with unittest.mock.patch('app.db.session.commit', side_effect=Exception('Database connection error')):
                response = self.client.post('/api/users', json={
                    'firstname': 'John',
                    'lastname': 'Doe',
                    'email': 'john.doe@example.com',
                    'phone': '1234567890',
                    'age': 25,
                    'password': 'password123'
                }, follow_redirects=True)
                self.assertEqual(response.status_code, 500)
                self.assertIn('Database connection error', response.get_json()['message'])
    
if __name__ == '__main__':
    unittest.main()