#!/usr/bin/python

import sys
#                   $1  ,   .10
def making_change(amount, denominations):
  # divide amount by denominations? multiply?
  for i in range(len(amount)-1):
  pass 


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")