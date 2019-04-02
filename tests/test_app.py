import unittest
from FlaskApp.app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        data = response.get_data(as_text=True)
        data = data.encode('ascii')
        assert b"Welcome to InterSystems Corporation" in data
        assert b"Contents:" in data
        assert b"Click here to receive container information sending to your email" in data
        assert b"Click here to reset password" in data
        assert b"Login" not in data
        assert b"Logout" not in data

    def test_reset_password_request(self):
        response = self.app.get('/reset_password')
        self.assertEqual(response.status_code, 200)

        data = response.get_data(as_text=True)
        data = data.encode('ascii')
        assert b"Reset Password" in data
        assert b"Email" in data
        assert b"InterSystems Corporation" in data
        assert b"New Password" not in data
        assert b"Confirm Password" not in data

    def test_reset_password(self):
        response = self.app.get('/reset_password/<user>')
        self.assertEqual(response.status_code, 200)

        data = response.get_data(as_text=True)
        data = data.encode('ascii')
        assert b"Password" in data
        assert b"InterSystems Corporation" in data
        assert b"Welcome to" not in data
        assert b"Email" not in data

    def test_send_email(self):
        response = self.app.get('/email')
        self.assertEqual(response.status_code, 200)

        data = response.get_data(as_text=True)
        data = data.encode('ascii')
        assert b"Sent email about container successfully." in data
        assert b"If you want to return to your lab, you can use this link" not in data
        assert b"Reset Password" not in data
        assert b"Confirm Password" not in data
