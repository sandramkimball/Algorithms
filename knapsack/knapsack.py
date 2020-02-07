#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

                            # 30
def knapsack_solver(items, capacity):
  total_size = 0
  max_cap = []
  item_combos = []
  
  #recursive - calculate maximized carrying capacity options  
  #save combos to arr that fall within capacity
  if items == 0:
    return 0
  if items == 1:
    while total_size <= capacity:
      if total_size + items.size <= capacity:
        total_size += items.size
      return total_size
    return 1  
    
  item_combos.append( knapsack_solver(items, capacity-items.size) )       
  
  #add? multiply? compare all combos
  #now check for which arr has the highest value? recursive sort func?
  total_value = 0

  def value_func(i):
     total_value += i.value

  for i in item_combos:
    if value_func(i) > value_func(i+1):
      max_cap = i
    
  return max_cap
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')