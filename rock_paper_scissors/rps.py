#!/usr/bin/python

import sys

def rock_paper_scissors(n, cache=None):
  if n < 0:
    return 0
  if n == 0:
    return 1
  elif cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache={i: 0 for i in range(n+1)}
    plays = + rock_paper_scissors(n-2, cache) + rock_paper_scissors(n-3, cache)
    cache[n] = plays
  return plays

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

