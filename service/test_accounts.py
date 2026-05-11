import unittest
from service.account import app

class TestAccounts(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        # reset data
        from service.account import accounts, next_id
        accounts.clear()
        next_id = 1

    def test_create_account(self):
        res = self.client.post('/accounts', json={'name':'a','email':'a@b.com'})
        self.assertEqual(res.status_code, 201)
