#!/usr/local/bin/python3
import sys
import os

if len(sys.argv) == 4 :
    os.system("/usr/local/bin/code -n --wait --diff " + sys.argv[1] + " " + sys.argv[2])
if len(sys.argv) == 5 :
    os.system("/usr/local/bin/code -n --wait " + sys.argv[4])