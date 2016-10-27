import urllib

# open and read website
uf = urllib.urlopen('http://google.com')
uf.read()

# retrieve url from website
urllib.urlretrieve('http://google.com/logo.gif', 'blah.gif')
