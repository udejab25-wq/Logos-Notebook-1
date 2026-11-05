"""Serve this folder at http://localhost:8080 so the app can be tested and installed on this computer."""
import functools
import http.server
import mimetypes
import os
import webbrowser

mimetypes.add_type("application/manifest+json", ".webmanifest")
mimetypes.add_type("text/javascript", ".js")
PORT = 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


print(f"Logos Notebook is running at http://localhost:{PORT}  (press Ctrl+C to stop)")
try:
    webbrowser.open(f"http://localhost:{PORT}")
except Exception:
    pass
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), functools.partial(Handler)).serve_forever()
