import urllib.request 
from os import execlp

def download_file(url, path):
    try:
        if url [-4:] == ".txt":
            urllib.request.urlretrieve(url, path)
        else:
            raise NameError("Incorrect URL name")
    except:
            return "No txt file found in the given URL"
        
download_file("https://ia802707.us.archive.org/1/items/macbeth02264gut/0ws3410.txt","p")      