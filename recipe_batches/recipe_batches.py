#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients, cache=None):
  batches = 0
  
  for i in range(0, len(ingredients)):
    for j in range(0, len(recipe)):
      ingredients[i].v = ingredients[i].v - recipe[j].v
      if 0 not in ingredients:
        batches += 1
        recipe_batches(recipe, ingredients)
      else:
        return batches

  return batches


if __name__ == '__main__':
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))