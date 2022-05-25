@type.__call__
class Main():
    from libs import imports

    def __init__(s):
        s.l = s.imports()
        s.log = s.l.LOGGING()
        s.l = s.l.__return__()

        s.Handler = s.l.http.server.SimpleHTTPRequestHandler

        s.__main__()

    def __main__(s):
        s.PORT = s.args().p
        try:
            with s.l.socketserver.TCPServer(("", s.PORT), s.Handler) as httpd:
                s.log.info("serving at port " + str(s.PORT) + f"\nLink to server: http://localhost:{s.PORT}/")
                s.l.web.open(f"http://localhost:{s.PORT}/")
                httpd.serve_forever()
        except KeyboardInterrupt as e:
            s._except(e)
        except Exception as e:
            s._except(e)

    def args(s):
        parser = s.l.argparse.ArgumentParser(description='Create HTTP server on folder')
        parser.add_argument('-p', default=8000, type=int, help='Set port to server (default: 8000)')
        return parser.parse_args()
    
    def __return__(s):
        return s
    
    def _except(s, e):
        s.log.fatal(f"Can not start serverving at port {s.PORT}\nHave error: <{e}>")

        s.l.eg.GoogleE(s.l, s.log).search("Python error " + str(e))
        s.l.exit(0)
