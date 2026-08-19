from collections import deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        ingredient_to_recipes = {}
        in_degree = {}
        
        for recipe, ingredient_list in zip(recipes, ingredients):
            in_degree[recipe] = len(ingredient_list)
            for ingredient in ingredient_list:
                if ingredient not in ingredient_to_recipes:
                    ingredient_to_recipes[ingredient] = []
                ingredient_to_recipes[ingredient].append(recipe)

        queue = deque(supplies)
        possible_recipes = set(supplies)
        
        result = []
        while queue:
            item = queue.popleft()
            
            if item in in_degree and in_degree[item] == 0:
                result.append(item)
            
            if item in ingredient_to_recipes:
                for recipe in ingredient_to_recipes[item]:
                    in_degree[recipe] -= 1
                    if in_degree[recipe] == 0:
                        queue.append(recipe)
                        possible_recipes.add(recipe)

        return result
