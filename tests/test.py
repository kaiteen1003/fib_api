from flask_testing import TestCase
from responses import RESPONSE_N_MISSING, RESPONSE_N_NOT_DIGIT, RESPONSE_N_NEGATIVE
from main import app
import unittest


class MyTest(TestCase):

    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_n_correct(self):
        response = self.client.get("/fib?n=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"result": 5})

    def test_n_missing(self):
        response = self.client.get("/fib?n=")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, RESPONSE_N_MISSING)

    def test_n_notdigit(self):
        response = self.client.get("/fib?n=1o")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, RESPONSE_N_NOT_DIGIT)

    def test_n_negative(self):
        response = self.client.get("/fib?n=0")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, RESPONSE_N_NEGATIVE)


if __name__ == "__main__":
    # 「TestCase」という名前を継承したクラス(Mytest)の中の関数のうち、
    # 「test」が頭についている関数をすべて実行
    unittest.main()
