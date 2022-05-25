class imports():
    import socketserver
    import urllib
    import http.server
    from http.client import HTTPConnection
    import webbrowser as web

    import argparse
    import logging
    import requests
    
    from sys import exit
    from rich.logging import RichHandler
    from bs4 import BeautifulSoup

    import ErrorGoogle as eg

    def __init__(s) -> None:
        s.names = list(s.__dict__.keys())
    
    def LOGGING(s):
        FORMAT = "%(message)s"
        s.logging.basicConfig(
            level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[s.RichHandler()]
        )

        log = s.logging.getLogger("rich")
        s.HTTPConnection.debuglevel = 2

        return log

    def __return__(s):
        return s
