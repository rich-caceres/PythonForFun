from urlib.request import urlopen

url= "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"
page = urlopen

html_bytes = page.read()
html = html_bytes.decode("utf-8")
