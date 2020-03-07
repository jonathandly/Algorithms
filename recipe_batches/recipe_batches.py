#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  count = 0

  for key, val in recipe.items():
    for key2, val2 in ingredients.items():
      if val2 < val:
        return count 
      elif val != val2:
        return count
      elif val2 >= val and val2 // val > 0:
        count += 1

  return count


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 2, 'butter': 20, 'sugar': 40 }
  ingredients = { 'milk': 2, 'butter': 40, 'sugar': 80}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))