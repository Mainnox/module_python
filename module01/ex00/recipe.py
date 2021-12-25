class Recipe:
    """
    This is a class for handle recipe with simple arguments.

    Attributes:
        name (str):         The name of the recipe
        cooking_lvl (int):  The difficulty of the recipe (1 - 5)
        cooking_time (int): The time required for the recipe
        ingredients (list): The list of the ingredients
        description (str):  The description of the recipe
        recipe_type (str):  The type of meal (starter, lunch, dessert)
    """

    name = ""
    cooking_lvl = 0
    cooking_time = 0
    ingredients = {}
    description = ""
    recipe_type = ''
    def __init__(self, name: str, cooking_lvl: int,
                    cooking_time: int, ingredients: list,
                    recipe_type: str, description = "") -> None:
        """
        The constructor for Recipe class.
        (Only the description is optionnal)

        Attributes:
            name (str):         The name of the recipe
            cooking_lvl (int):  The difficulty of the recipe (1 - 5)
            cooking_time (int): The time required for the recipe
            ingredients (list): The list of the ingredients
            recipe_type (str):  The type of meal (starter, lunch, dessert)
            description (str):  The description of the recipe
        """
        print(type(cooking_lvl))
        print(cooking_lvl < 6 and cooking_lvl > 0)
        if (type(name) != type('')):
            print("The name should be a str!")
            print(Recipe.__init__.__doc__)
            exit(0)
        if ((type(cooking_lvl) != type(1)) or (cooking_lvl > 5 or cooking_lvl < 1)):
            print("The cooking_lvl have to be a int between 1 and 5")
            print(Recipe.__init__.__doc__)
            exit(0)
        if (type(cooking_time) != type(1) or cooking_time < 0):
            print("The cooking_time have to be a possitive int!")
            print(Recipe.__init__.__doc__)
            exit(0)
        if (type(ingredients) == type(list)):
            for i in ingredients:
                if (type(ingredients[i] != type(''))):
                    print("The ingredients have to be a list of string")
                    print(Recipe.__init__.__doc__)
                    exit(0)
        if (type(recipe_type) != type('') or (recipe_type != "dessert"\
            and recipe_type != "lunch" and recipe_type != "starter")):
            print("Recipe_type should be a \"dessert\", \"lunch\" or \"starter\"")
            print(Recipe.__init__.__doc__)
            exit(0)
        if (type(description) != type('')):
            print('Description should be empty or a string')
            print(Recipe.__init__.__doc__)
            exit(0)
        
        pass