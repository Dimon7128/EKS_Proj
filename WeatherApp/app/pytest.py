import unittest
import requests


APP_ADDR = "http://13.38.244.199/"

# Asserts a 200 response code from the weather web app using requests module


class AppConectivityTest(unittest.TestCase):

    def test_connection(self):
        response = requests.get(APP_ADDR, timeout=10).status_code
        self.assertEqual(response, 200, "Web app is not r eachable :( )")


if __name__ == "main":
    unittest.main()
