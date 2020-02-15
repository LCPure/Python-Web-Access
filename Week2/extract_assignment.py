import re

retrieve = open('regex_sum_179678.txt')
for line in retrieve:
    line = line.rstrip()
    zsum = re.findall('[0-9]+', line)
    zsum = [int(i) for i in zsum]
    if len(zsum) > 0:
        print(zsum)
