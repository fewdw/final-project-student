import unittest
import requests

class TestCredentialsAPI(unittest.TestCase):
    def test_credentials_api(self):
        url = "http://127.0.0.1:5001/credentials"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 3)

class TestCredentialAPI(unittest.TestCase):
    def test_credential_api(self):
        url = "http://127.0.0.1:5001/credentials/63cb4b50a315a6934e87c1bb"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIsInstance(data, dict)

class TestPostCredentialAPI(unittest.TestCase):
    def test_post_credential_api(self):
        url = "http://127.0.0.1:5001/credentials"
        payload = {
            "email": "email",
            "hash": "pw_hash",
            "lang": "lang",
            "type": "session_type"
        }
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("added credential with id", data)
        credential_id = data["added credential with id"]

    class TestPutCredentialAPI(unittest.TestCase):
        def test_put_credential_api(self):
            url = "http://127.0.0.1:5001/credentials"
            payload = {
                "id": credential_id,
                "email": "email",
                "hash": "pw_hash",
                "lang": "lang",
                "type": "session_type"
            }
            response = requests.put(url, json=payload)
            self.assertEqual(response.status_code, 200)
    
    class TestDeleteCredentialAPI(unittest.TestCase):
        def test_delete_credential_api(self):
            url = "http://127.0.0.1:5001/credentials"
            payload = {"id": credential_id}
            response = requests.delete(url, json=payload)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
