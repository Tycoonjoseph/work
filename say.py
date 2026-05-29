# install the packages using pip like now i am using the pip install cowsay
import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    cowsay.trex("Hello, " + sys.argv[1])
    cowsay.dragon("Hello, " + sys.argv[1])
    