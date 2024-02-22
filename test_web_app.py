from app import app
import unittest


class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()

    def tearDown(self):
        self.app_ctxt.pop()
        self.app = None
        self.app_ctxt = None

    def test_app(self):
        assert self.app is not None
        assert app == self.app