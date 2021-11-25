def add_recipe():
    print('test1')

def delete_recipe():
    print('test2')

def print_recipe():
    print('test3')

def print_cookbook():
    print('test4')

def quit():
    print('\nCookbook closed.')
    exit(0)

if __name__ == "__main__":
    check = -1
    while (True):
        try:
            check = int(input('Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n'))
        except:
            continue
        if (check >= 0 and check <= 5):
                options = {1 : add_recipe, 2 : delete_recipe, 3 : print_recipe, 4 : print_cookbook, 5 : quit}
                options[check]()
    