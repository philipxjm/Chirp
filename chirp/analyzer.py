from urllib.parse import urlencode
from urllib.request import Request, urlopen

def analyze(sentence):
    url = "http://text-processing.com/api/sentiment/"
    post_fields = {'text': sentence}
    request = Request(url, urlencode(post_fields).encode())
    json = urlopen(request).read().decode()

    return json