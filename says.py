import sys
# import the hello function from the saying libabry module
from saying import hello
if len(sys.argv)  == 2:
    hello(sys.argv[1])