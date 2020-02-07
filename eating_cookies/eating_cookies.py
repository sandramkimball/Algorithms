#!/usr/bin/python

import sys

# The cache parameter is to implement a solution that is more efficient than recursive solution.
# Factorial Function?
def eating_cookies(n, cache=None):
  ways=1
  if n in cache.keys():
    return cache[n]
    
  for i in range(1, n+1):
    ways *=i
  
  cache[n] = ways
  return ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
  
print(eating_cookies(5))
