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
      if line.startswith("!"):
        line = line.lstrip("!")
      line = line.strip()

      p = subprocess.Popen(["host", "-T", "A", line],
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,
                           close_fds=True)
      p.stdin.close()
      p.poll()
      res = p.stdout.read()
      if (res == None) or (res == ""):
        outfh.write(line + "\n")
      else:
        outfh.write("// " + line + " has A record.")

infh.close()
outfh.close()
