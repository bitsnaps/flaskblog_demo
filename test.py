from flaskblog import create_app
import unittest

app = create_app()
app.config['TESTING'] = True
# Here we needed to deactivate the CSRF protection for testing
app.config['WTF_CSRF_ENABLED'] = False

class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        # print("code: " + str(response.status_code))
        self.assertEqual(response.status_code, 200)

    # Ensure that flask was set up correctly
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        # print(response.data.decode('utf-8'))
        self.assertTrue(b'Login In' in response.data)

    # Ensure for correct login
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="admin@example.com",
                        password="admin"), follow_redirects=True
        )
        self.assertIn(b'Account', response.data)

    # Ensure for incorrect login
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="admin@example.com",
                        password="test"), follow_redirects=True
        )
        self.assertIn(b'Login Unsuccessfull', response.data)

if __name__ == '__main__':
    unittest.main()
