from urllib.request import urlopen
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    print(attr[1])

def getSource(url):
    response = urlopen(url)
    html = response.read()
    return html.decode()

html = getSource("https://www.uol.com.br")
#print(html)

parser = MyParser()
parser.feed(html)


