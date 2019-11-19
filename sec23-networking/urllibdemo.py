import urllib.request

# Request a web page and read its content
try:
    url = urllib.request.urlopen("http://www.google.es/")
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print("The web page is not found")
    exit()

# Write the content in one file
f = open('google.html', 'wb')
f.write(content)
f.close
