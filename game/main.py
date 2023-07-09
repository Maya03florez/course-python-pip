import random

def choose_option():
    option = ('rock','paper','scissor')
    user_option = input('Write an option => ')

    if not user_option  in option:
        print('That option is not available')
        return None, None
    
    computer_option = random.choice(option)

    print('user option', user_option)
    print('computer option', computer_option)
    return user_option,computer_option

def check_rules(user_option,computer_option,user_wins,computer_wins):
    if user_option == computer_option:
        print('tie')
    elif user_option == 'rock' and computer_option == 'scissor':
        print('win')
        user_wins += 1
    elif user_option == 'paper' and computer_option == 'rock':
        print('win')
        user_wins += 1
    elif user_option == 'scissor' and computer_option == 'paper':
        print('win')
        user_wins += 1
    else:
        print('loose')
        computer_wins += 1
    return user_wins,computer_wins

def run_game():
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:
        print('=' * 10)
        print('Rounds',rounds)
        print('=' * 10)

        print('user wins', user_wins)
        print('computer wins', computer_wins)
        rounds += 1
        
        user_option,computer_option = choose_option()
        user_wins,computer_wins = check_rules(user_option,computer_option,user_wins,computer_wins)

        if computer_wins == 2:
            print('The winner is the computer')
            break

        if user_wins == 2:
            print('The winner is the user')
            break

if __name__ == '__main__':
    run_game()