import os
import sys

i = sys.argv[3]
o = open(sys.argv[4], 'w')
query = sys.argv[2]
prog = sys.argv[1]
print("usage: python3 shodanam.py pathtoprogram query in.txt out.txt")
print("example: python3 shodanam.py \"enum4linux -a\" \"Authentication: disabled' port:445 database\" in.txt out.txt")
print("python3 shodanam.py \"nmap -v -A\" \"board of\" in.txt out.txt")

os.system('shodan download '+i+' '+query)
os.system('shodan parse --fields ip_str '+i+'.json.gz > '+i)
with open(i, 'r') as file:
    for line in file:
        thing = os.popen(prog+' '+line).read()
        print(thing)
        print(thing, file=o)
