#!/usr/bin/python

import sys

def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  if n == 0:
    return 1
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {0: 1 for i in range(n+1)}
    value = eating_cookies(n-1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cach)
    cache[n] = value
    return value


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
  
print(eating_cookies(5))
