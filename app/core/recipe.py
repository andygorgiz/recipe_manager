class Recipe:
    def __init__(self, name: str, ingredients: str, instructions: str):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    
    def to_dict(self):
        return{
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }