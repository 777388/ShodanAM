# ShodanAM
Ground work automation for running any number of programs over a list compiled through shodan

usage: python3 shodanam.py pathtoprogram options query

example: python3 shodanam.py enum4linux "-a" "Authentication: disabled' port:445 database"

python3 shodanam.py nmap "-v -A" "board of"

just be sure that the options lead up to the IP at the end of the program call.

Output will be sent to out.txt, IP list will be sent to in.txt
