import re

retrieve = open('regex_sum_179678.txt')
inp = retrieve.read() #create file buffer
zsum = re.findall('[0-9]+', inp) #search for integers
zsum = [int(i) for i in zsum] #convert number strings to integers
if len(zsum) > 0:
  print(zsum) #print list of integers
  print("The sum of the numbers in the file is ", sum(zsum)) #print string
