from os import EX_CANTCREAT


def add_recipe(cookbook):
    recipe_name = str(input('What\'s the name of your new recipe ?\n'))
    recipe = {}
    ingredients = []
    while (True):
        try:
            i = int(input('How many ingredients the recipe have ?\n'))
        except:
            print('\nERROR\nPlease enter a number\n')
            continue
        break
    for i in range(0, i):
        ingredients.append(input('What is your ingredients number {} ?\n'.format(i + 1)))
    recipe['ingredients'] = ingredients
    recipe['meal'] = input('What kind of meal it is ?\n')
    while (True):
        try:
            recipe['prep_time'] = int(input('How many time you need to prepare this recipe ?\n'))
        except:
            print('\nERROR\nOnly number please.\n')
            continue
        break
    while (True):
        print('\nRECAPITULATION:\nNew recipe: {}\nIngredients list: {}\nType of meal: {}\nPreparation Time: {}\n'.format(recipe_name, str(ingredients), recipe['meal'], recipe['prep_time']))
        ret = input('Enter \'Save\' to save the new recipe or \'Abort\' to abort it\n')
        if (ret == 'Save'):
            cookbook[recipe_name] = recipe
            print('Your recipe was saved with succes!\n\n')
            break
        elif (ret == 'Abort'):
            print('Your recipe was aborted with succes!\n\n')
            break

def delete_recipe(cookbook):
    if (len(cookbook) == 0):
        print('ERROR no recipe to delete\n\nABORT\n')
        return
    while True:
        print('Please select one of those recipe to delete')
        for key in cookbook:
            print(key)
        s = input()
        if cookbook.get(s):
            break
        print('\nWrong recipe name\n')
    while True:
        confirmation = input('Are you sure to want to delete {}\'s recipe ? (Y/N)'.format(s))
        if confirmation == 'Y':
            break
        elif confirmation == 'N':
            print('\nDelete has been canceled\n')
            return
        print('Enter Y for Yes and N for No')
    cookbook.pop(s)
    print('{}\'s recipe has been successfully deleted\n'.format(s))

def print_recipe(cookbook):
    if (len(cookbook) == 0):
        print('ERROR no recipe to print\n\nABORT\n')
        return
    while True:
        print('Please select one of those recipe to print')
        for key in cookbook:
            print(key)
        s = input('\n')
        if cookbook.get(s):
            break
        print('\nWrong recipe name\n')
    print('Guide line for your {}'.format(s))
    print('Ingredients list: {}\nTo be eaten for {}\nTakes {} minutes of preparation\n'.format(cookbook[s]['ingredients'], cookbook[s]['meal'], cookbook[s]['prep_time']))

def print_cookbook(cookbook):
    if (len(cookbook) == 0):
        print('ERROR no recipe to print\n\nABORT\n')
        return
    print('\nThe cookbook have {} recipes:\n'.format(len(cookbook)))
    for key in cookbook:
        print(key)
    print('\n')

def quit(cookbook):
    print('\nCookbook closed.')
    exit(0)

if __name__ == "__main__":
    #Args aren't like the subject``
    check = -1
    cookbook = {'cake' : {'ingredients' : ['flour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : 60},
                'sandwich' : {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'], 'meal' : 'lunch', 'prep_time' : 10},
                'salad' : {'ingredients' : ['avocado', 'arugula', 'tomatoes' ,'spinach'], 'meal' : 'lunch', 'prep_time' : 15}}
    while (True):
        try:
            check = int(input('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n'))
        except:
            continue
        if (check >= 0 and check <= 5):
                options = {1 : add_recipe, 2 : delete_recipe, 3 : print_recipe, 4 : print_cookbook, 5 : quit}
                options[check](cookbook)
