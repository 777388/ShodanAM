import os
import sys

def func(value):
    return ''.join(value.splitlines())
i = in.txt
b = '200'
o = open(out.txt, 'w')
query = sys.argv[3]
prog = sys.argv[1]
options = sys.argv[2]
print("usage: python3 shodanam.py pathtoprogram options query")
print("example: python3 shodanam.py enum4linux '-a' `'Authentication: disabled' port:445 database`")

os.system('shodan download '+i+' '+query)
os.system('shodan parse --fields ip_str '+i+'.json.gz > '+i)
with open(i, 'r') as file:
    for line in file:
        thing = os.popen(prog+' '+options+' '+line).read()
        print(thing)
        print(thing, file=o)

