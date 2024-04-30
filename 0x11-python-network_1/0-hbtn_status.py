import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as url:
        read = url.read()
        print('Body response:')
        print("\t- type: {}".format(type(url)))
        print("\t- content: {}".format(url))
        print("\t- utf8 content: {}".format(url.decode('utf-8')))
