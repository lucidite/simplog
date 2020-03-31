from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site


class SimplogHome(Resource):
    isLeaf = True

    def render_GET(self, request):
        return "Hello, I'm Simplog!".encode('utf-8')


if __name__ == '__main__':
    root = SimplogHome()
    site_factory = Site(root)
    reactor.listenTCP(8080, site_factory)
    reactor.run()
