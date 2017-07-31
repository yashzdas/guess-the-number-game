from random import randint


def play_again():
    var= input('Type: "sure" or "exit" ')
    if var == "sure":
        play()
    elif var == "exit":
        print('see you again..!')
        exit()
    else:
        print('keyword not matching')
        play_again()
def play():
    user= int(input('Guess a digit between 0 to 9: '))
    comp= randint(0,10)
    if user == comp:
        print("win it's",comp)
    elif user<comp:
        z= str(comp-user)
        print("It's",comp,' your number is '+z+' digit lower')
    elif comp<user:
        x= str(user-comp)
        print("It's",comp,' your number is '+x+' digit higher')
        print('shall we play again..!')
    play_again()
play()
