import json

serviceurl = input('Enter URL for JSON file ')

# Ignore SSL certificate errors

url = serviceurl
print('Retrieving', url)
with open('http://py4e-data.dr-chuck.net/comments_42.json', 'r') as readfile:
    info = json.load(readfile)
    #total_count = 0 #intialize sum to zero
for item in info: #loop through all the count data
    print("number of people", item['count'])
    #indivcount = item['count']
    #num_count = int(indivcount) #convert count string to integer
    #total_count = total_count + num_count #Sum all the comment counts

#print('Total Count is ', total_count) #display the sum
