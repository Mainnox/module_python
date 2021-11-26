from random import randint

if __name__ == "__main__":
    print('This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType \'exit\' to end the game.\nGood luck!')
    answer = randint(1, 99)
    number_attempt = 0
    while True:
        user = input('\n')
        if (user == 'exit'):
            print('Thanks for playing!\nGoodbye.')
            break
        try:
            u_input = int(user)
            number_attempt += 1
        except:
            print('That\'s not a number.')
            continue
        if u_input < answer:
            print('Too low!')
        elif u_input > answer:
            print('Too high!')
        else:
            if (answer == 42):
                print('The answer to the ultimate question of life, the universe and everything is 42.')
            if (number_attempt == 1):
                print('Congratulations! You got it on your first try!')
            else:
                print('Congratulations. you\'ve got it!\nYou won in {} attempts!'.format(number_attempt))
            break
        
    