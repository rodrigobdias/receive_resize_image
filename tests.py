import unittest
from upload_image import app


class TestApi(unittest.TestCase):

    def test_get(self):
        self.app = app.test_client()
        response = self.app.get('/input')
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()