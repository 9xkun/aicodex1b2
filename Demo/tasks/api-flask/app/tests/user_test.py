import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import create_app

# test_user_controller.py

class TestUserController(unittest.TestCase):
    def setUp(self):
        # python server
        self.app = create_app()

        # python browser
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_create_user_valid(self):
        response = self.client.post('/api/users', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'email': 'john.doe1@example.com',
            'phone': '1234567890',
            'age': 25,
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_create_user_missing_email(self):
        response = self.client.post('/api/users', json={
            'firstname': 'John',
            'lastname': 'Doe',
            'phone': '1234567890',
            'age': 25,
            'password': 'password123'
        }, follow_redirects=True)
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

    
if __name__ == '__main__':
    unittest.main()