#!/usr/bin/env python

import sys
import socket
import string
import subprocess

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
      line = line.lstrip("!")
      line = line.strip()
      #print "Querying " + line
      p = subprocess.Popen(["host", "-t", "A", line],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,
                           close_fds=True)
      p.stdin.close()
      p.poll()
      res = p.stdout.read()
      # print res
      #print "address" in res
      if not ( "address" in res ):
        print line + " has NO A record."
        outfh.write(line + "\n")
      else:
        print "// " + line + " has A record."
        outfh.write("// " + line + " has A record.\n")

infh.close()
outfh.close()
