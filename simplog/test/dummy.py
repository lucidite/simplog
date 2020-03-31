# Reference: Testing Twisted Web Resources, https://bit.ly/2JvuMhA

from twisted.internet.defer import succeed
from twisted.web.server import Site
from twisted.web.test.test_web import DummyRequest


class SimplogDummyRequest(DummyRequest):
    def __init__(self, method, url, args=None, headers=None):
        super().__init__(url.split('/'))
        self.method = method

        if headers:
            for name, values in headers.items():
                # self.setHeader(name, values)
                self.headers.update(headers)
        if args:
            for arg_key, arg_value in args.items():
                self.addArg(arg_key, arg_value)

    def value(self):
        return "".join(elem.decode('utf-8') for elem in self.written)


def _resolve_result(request, result):
    if isinstance(result, bytes):
        request.write(result)
        request.finish()
        return succeed(request)
    elif isinstance(result, str):
        request.write(result.encode('utf-8'))
        request.finish()
        return succeed(request)
    else:
        raise ValueError(f"Unexpected result: {result}")


class DummySite(Site):
    def get(self, url, args=None, headers=None):
        return self._request("GET", url, args, headers)

    def post(self, url, args=None, headers=None):
        return self._request("POST", url, args, headers)

    def _request(self, method, url, args, headers):
        request = SimplogDummyRequest(method, url, args, headers)
        resource = self.getResourceFor(request)
        result = resource.render(request)
        return _resolve_result(request, result)
