import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as url:
    read = url.read()
