#!/usr/bin/env python

import sys
import socket
import string

if (len(sys.argv) != 3):
  print """
Usage: convert-to-public-suffices.py <infile> <outfile>
"""
  sys.exit(1)

infh = open(sys.argv[1], "r")
outfh = open(sys.argv[2], "w")


for line in infh:
    if line.startswith("*") or line.startswith("/") or (not "." in line):
      continue
    else:
      try:
        result = socket.gethostbyname(line)
      except Exception, e:
        outfh.write(line)
        continue
      outfh.write("// " + line + " has A record.")

infh.close()
outfh.close()
