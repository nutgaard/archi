import cgi, os, SocketServer, sys, time, urllib, re
from SimpleHTTPServer import SimpleHTTPRequestHandler
from StringIO import StringIO

class DirectoryHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        try:
            list = filter(lambda x:x.endswith(".jar"), os.listdir(path))
        except os.error:
            self.send_error(404, "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        f = StringIO()
        f.write("{\n")
        appendComma = False

        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
            
            if appendComma:
                f.write(',\n')

            mvnId = re.sub(r'-\d.*?\.jar$', '', linkname)

            appendComma = True
            f.write('\"%s\":\"%s\"' % (urllib.quote(mvnId), cgi.escape(displayname)))
        f.write("\n}")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "application/json; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f

httpd = SocketServer.TCPServer(("", 8000), DirectoryHandler)
print "serving at port", 8000
httpd.serve_forever()