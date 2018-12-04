from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import urllib.request
import hashlib
import os

url = input("Samsung link: ")
html = urlopen(url)
soup = bs(html.read())

download_links = {link['longdesc']:link['alt'] for link in soup.find_all('img') if link.has_attr('longdesc')}

output_dir = input("Output dir: ")

for url, file_name in download_links.items():
    file_path = os.path.join(output_dir, file_name)
    urllib.request.urlretrieve(url, file_path)
