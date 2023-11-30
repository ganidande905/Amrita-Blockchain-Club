import re
def check(eth_address):
    pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
    if pattern.match(eth_address):
        print("True")
    else:
        print("False")
check(eth_address=input("Enter: "))
#re.compile() function is used to compile a regular expression pattern into a regex object. 
# regex object represents a compiled version of a regular expression pattern,,,,it provides methods for pattern matching and various operations on strings