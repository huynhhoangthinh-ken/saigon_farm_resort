import http.server
import socketserver
import os
import mimetypes

PORT = 8300
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

mimetypes.init()
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/html', '.html')
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('application/json', '.json')
mimetypes.add_type('image/avif', '.avif')
mimetypes.add_type('image/webp', '.webp')
mimetypes.add_type('image/jpeg', '.jpg')
mimetypes.add_type('image/png', '.png')

class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Clean URL rewrite
        path = self.path.split('?')[0].rstrip('/')
        
        # Specific aliases for listing / shopping cart
        if path in ['/gio-hang', '/giohang', '/bang-gia', '/bang-hang', '/listing']:
            self.path = '/listing.html'
        elif not os.path.splitext(path)[1]: # no extension
            # Check if .html exists
            candidate = os.path.join(DIRECTORY, path.lstrip('/') + '.html')
            if os.path.isfile(candidate):
                self.path = path + '.html'
                
        return super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with http.server.ThreadingHTTPServer(('', PORT), CleanUrlHandler) as httpd:
        print(f'Saigon Farm Resort Server running at http://localhost:{PORT}/')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
