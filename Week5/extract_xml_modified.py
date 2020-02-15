import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

track = input('Enter - ')
#uh = urllib.request.urlopen(url)
#data = uh.read()
tree = ET.parse(track)
root = tree.getroot()
lstxml = tree.findall('comments/comment')
for item in lstxml:
    print('count', item.find('count').text)
