import os
import sys

i = 'in.txt'
o = open('out.txt', 'w')
query = sys.argv[2]
prog = sys.argv[1]
print("usage: python3 shodanam.py pathtoprogram query")
print("example: python3 shodanam.py \"enum4linux -a\" \"Authentication: disabled' port:445 database\"")
print("python3 shodanam.py \"nmap -v -A\" \"board of\"")

os.system('shodan download '+i+' '+query)
os.system('shodan parse --fields ip_str '+i+'.json.gz > '+i)
with open(i, 'r') as file:
    for line in file:
        thing = os.popen(prog+' '+line).read()
        print(thing)
        print(thing, file=o)
