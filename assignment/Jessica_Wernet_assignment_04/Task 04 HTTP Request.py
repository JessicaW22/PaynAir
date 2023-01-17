import urllib

def letters(word):
    return list(word)


def open_url(url):
    webUrl = urllib.request.urlopen(url)
    content = webUrl.read()
    count = 0
    characters = letters(content)
    charlist = []
    while count < 200:
        charlist.append(chr(characters[count]))
        count += 1 
    result = ''.join(str(x) for x in charlist)
    print(result)


open_url('https://de.wikipedia.org/wiki/Albert_Einstein%27)