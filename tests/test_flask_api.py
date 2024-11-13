import unittest
from main import app


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # This test mimics sending a post request to the route /chat
    def test_chat_post(self):
        # The prompt content is not important in this test. We want to test the status code of the response.
        response = self.client.post("/chat", json={"prompt": "How to use GitHub actions to deploy a Flask Application?"})
        self.assertEqual(response.status_code, 200)

    def test_chat_get(self):
        # Sending a request type that is not supported will result in HTTP status code of 405 (method not allowed)
        response = self.client.get("/chat")
        self.assertEqual(response.status_code, 405)
