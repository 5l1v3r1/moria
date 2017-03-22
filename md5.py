#!/usr/bin/env python

import hashlib
import sys

m=hashlib.md5()


if len(sys.argv) < 3:
  print "\nUsage:\n # "+sys.argv[0]+" [hashfile] [wordlist]\n"
  exit(1)
lines = []
words = []
with open(sys.argv[1]) as file:
  for line in file:
    line = line.strip() #or someother preprocessing
    lines.append(line)

with open(sys.argv[2]) as file:
  for line in file:
    line = line.strip()
    words.append(line)

for l in lines:
  x=l.split("$")
  passX=x[2]
  salt=x[1]
  user=x[0].split(":")[0]
#  print "Hash found as (user):"+user+",  (salt):"+salt+",  (hash):"+passX+"!\n"
  for f in words:
     xray=str(hashlib.md5(f).hexdigest())
     cmp=str(hashlib.md5(str(xray)+""+str(salt)).hexdigest())
     if cmp == passX:  
       print "[+] FOUND: "+user+"  "+f+"  "+cmp
       break
