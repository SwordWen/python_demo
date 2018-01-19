import httplib
params = ""
proxyHost = '127.0.0.1'
proxyPort = 8080

print "set proxy: {0}:{1}".format(proxyHost, proxyPort)
conn = httplib.HTTPConnection(proxyHost, proxyPort)
conn.request("POST", "http://www.google.com", params)

resp = conn.getresponse()

print "resp: " + str(resp.status)