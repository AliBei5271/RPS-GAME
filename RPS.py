import random


print('--------- RPS GAME ---------')


userScore = 5
cpuScore = 5


while userScore and cpuScore != 0:
    choises = ['rock', 'paper', 'scissors']
    randomChoise = random.randint(0, 2)
    c_choise = choises[randomChoise]

    user = input('pls enter your move  :  ')
    print(f"the cpu's move is    {c_choise}.")
    if user == 'paper' and c_choise == 'rock':
        print('++++++++ user win +++++++++')
        cpuScore -= 1
        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))
    elif user == 'paper' and c_choise == 'paper':
        print('tieeeeee')

        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))
    elif user == 'paper' and c_choise == 'scissors':
        print('------ user lost --------')
        userScore -= 1

        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))
    elif user == 'scissors' and c_choise == 'scissors':
        print('tieeeeee')

        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))
    elif user == 'scissors' and c_choise == 'paper':
        print('++++++++ user win +++++++++')
        cpuScore -= 1

        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))
    elif user == 'scissors' and c_choise == 'rock':
        print('------ user lost --------')
        userScore -= 1
        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))
    elif user == 'rock' and c_choise == 'scissors':
        print('++++++++ user win +++++++++')
        cpuScore -= 1
        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))
    elif user == 'rock' and c_choise == 'rock':
        print('tieeeeee')
        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))
    elif user == 'rock' and c_choise == 'paper':
        print('------ user lost --------')
        userScore -= 1
        print('your score is: ' + str(userScore))
        print('the cpu score is: ' + str(cpuScore))

    elif user not in choises:
        print('your answer is wrong.\nplease try again:')
        continue
