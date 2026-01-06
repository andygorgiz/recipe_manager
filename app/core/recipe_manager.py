from core.recipe import Recipe
from core.storage import load_recipes, save_recipes
from utils.logger import logger
from utils.input_validation import safe_input

logger = get_logger()

class RecipeManager:
    def __init__(self):
        self.recipes = load_recipes()

    def show_recipes(self):
        if not self.recipes:
            print("Inga recept finns.")
            return
        
        for recipe_number, recipe in enumerate(self.recipes, start=1):
            print(f"\n{recipe_number}. {recipe['name']}")
            print("Ingredienser:")
            for ingredient in recipe["ingredients"]:
                print(f" - {ingredient}")
            print("Instruktioner:")
            print(recipe["instructions"])
    
    def add_recipe(self):
        try: 
            name = safe_input("Receptnamn: ")
            ingredients = safe_input("Ingredienser (separera med kommatecken): ")
            instructions = safe_input("Instruktioner: ")

            ingredient_list = [
                i.strip() for i in ingredients.split(",")
            ]

            recipe = Recipe(name, ingredient_list, instructions)
            self.recipes.append(recipe.to_dict())
            save_recipes(self.recipes)

            logger.info(f"Recept tillagt: {name}")
            print("Recept tillagt!")

        except ValueError  as e :
            logger.warning(str(e))
            print(e)
    
    def remove_recipes(self):
        self.show_recipes()
        try:
            choice = int(safe_input("Ange numret på receptet du vill ta bort: "))
            removed = self.recipes.pop(choice - 1)
            save_recipes(self.recipes)

            logger.info(f"recept borttaget: {removed['name']}")
            print("Recept borttaget!")

        except (ValueError, IndexError):
            logger.error("Fel vid borttagning av recept")
            print("Ogiltigt val.")
    

    def run(self):
        while True:
            print("\n1. Visa recept")
            print("2. Lägg till recept")
            print("3. Ta bort recept")
            print("4. Avsluta")

            choice = input("Välj: ")
            
            if choice == "1":
                self.show_recipes()
            elif choice == "2":
                self.add_recipe()
            elif choice == "3":
                self.remove_recipes()
            elif choice == "4":
                print("Hejdå!")
                break
            else:
                print("Ogiltigt val.")

