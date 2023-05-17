from urllib.request import urlopen

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource("http://www.uol.com.br")
print(html)