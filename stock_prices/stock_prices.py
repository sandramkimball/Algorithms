#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if prices in cache.keys():
    return cache[prices]

  if prices == 0:
    return 0
  if prices == 1:
    return 1

  profit = find_max_profit(prices-1) + find_max_profit(prices-2)
  cache[prices] = profit
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))