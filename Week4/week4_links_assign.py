# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

position = int(17)
count = int(7)

fndUrl = input('Enter - ')
for i in range(count): #loop count times from position
    html = urllib.request.urlopen(fndUrl).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve the starting position tag
    fndUrl = soup('a')[position].get('href', None)
    print(fndUrl)
