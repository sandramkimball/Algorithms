#!/usr/bin/python

import sys
# Example: `making_change(10)` should return 4, since there are 4 ways to make
# change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

#  1. We can make change for 10 cents using 10 pennies
#  2. We can use 5 pennies and a nickel
#  3. We can use 2 nickels
#  4. We can use a single dime
 
def making_change(amount, denominations):
  ways = 0
  all_denoms = [50, 25, 10, 5, 1]

  if denominations:
    for i in denominations:
      if amount % i == 0:
        ways += 1
  else:     
    for i in all_denoms:
      if amount % i == 0:
        result += 1
  return ways

if __name__ == "__main__":
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")