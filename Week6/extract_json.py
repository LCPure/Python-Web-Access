import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = input('Enter URL for JSON file ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = serviceurl
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')
print(data)
info = json.loads(data)
print(type(info)) #for debug use
print('Json loaded', info) #print out json data
wow = info['comments'] #load actual data from dictionary

#print('User count:', len(wow)) #output number of users
bang = 0
total_count = 0 #intialize sum to zero
limit = len(wow)
for item in range(limit): #loop through all the count data
    print('Alpha')
    print("number of people", wow[bang]['count']) #print the count value for every person
    summing_comments = int(wow[bang]['count'])
    total_count = total_count + summing_comments #sum the counts
    bang = bang + 1



print(info)
print(len(info))
print('Total Count is ', total_count) #display the sum
