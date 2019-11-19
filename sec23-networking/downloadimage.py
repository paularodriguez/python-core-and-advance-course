import urllib.request

url = "http://www.gstatic.com/webp/gallery3/1.png"

urllib.request.urlretrieve(url, "flower.png")
