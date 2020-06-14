# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
input_list=[]

for line in sys.stdin:
    input_list.append(line)

n = int(input_list[0])
entries = input_list[1:n+1]
queries = input_list[n+1:]

phoneBook = {}

for entry in entries:
    name, id = entry.split()
    phoneBook[name] = id

for query in queries:
    stripQuery = query.rstrip()
    if stripQuery in phoneBook:
        print(stripQuery + "=" + str(phoneBook[stripQuery]))
    else:
        print("Not found")
