#!/usr/bin/python

import argparse

cache = {}

def find_max_profit(prices, cache=None):
  if prices == 0:
    return 0
  if prices == 1:
    return 1
  elif cache and cache[prices] > 0:
    return cache[prices]
  else: 
    if not cache: 
      cache = {num: 0 for num in range(prices + 1)}
    profit = find_max_profit(prices-1, cache) + find_max_profit(prices-2, cache) + find_max_profit(prices-3, cache)
    cache[prices] = profit
  print( profit)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))