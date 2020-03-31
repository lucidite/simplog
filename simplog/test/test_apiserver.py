from twisted.trial import unittest
from twisted.internet.defer import inlineCallbacks

from simplog.apiserver import SimplogHome
from simplog.test.dummy import DummySite


class SimplogTestCase(unittest.TestCase):
    def setUp(self):
        self.web = DummySite(SimplogHome())

    @inlineCallbacks
    def test_GET_root_returns_success(self):
        response = yield self.web.get('')
        self.assertIn(response.responseCode, [200, None], 'GET / should return 200 OK')

    @inlineCallbacks
    def test_GET_returns_hello(self):
        response = yield self.web.get('')
        self.assertEquals(response.value(), "Hello, I'm Simplog!")
