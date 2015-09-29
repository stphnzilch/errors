#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys
import os
def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision\n")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
  
   assert 9 == 10, "9 and 10 arn't equil"    

elif error_type == "io":
    open('blah_blah-blah') 
elif error_type == "import":
    from that_file.the_stuff import the_stuff

elif error_type == "shoes":
       socks = "nike"
       if socks != "addidas":
           raise "shoes"

elif error_type == "index":
    gmo = "GMO4EVA"
    a= gmo[666]
elif error_type == "key":
    organic = {"n" : 1, "o" : 2, "g" : 3,"o" : 4, "o" : 5,"d" : 6}
    print organic[9]
elif error_type == "name":
    n=rope()
    n.nope()
    class rope:
        def nope():
            print nope
elif error_type == "os":
    
    os.ttyname(7)
elif error_type == "type":
    'cow'**2
elif error_type == "value":
    print(int('rrrr'))
elif error_type == "zerodivision":
    print 1/0
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
