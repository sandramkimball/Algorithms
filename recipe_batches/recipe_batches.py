#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  enough_ing = []
  # i = recipe[i]
  # j = ingredients[j]

  for k, v in recipe:
   for k, v in ingredients:
     if recipe.k == ingredients.k:
      #now we gotta check if we have enough of ingredient.
      #mybe save to arr? to keep track if all opts divide once or not?
      if recipe.v - ingredients.v > 0:
         enough_ing.append(1)
      else:
        enough_ing.append(-1)

  for i in enough_ing:
    if i == -1:
      return False
    else: 
      batches += 1

  return batches


if __name__ == '__main__':
  # Change these entries to test with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }

  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))