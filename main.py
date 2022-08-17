from game import Game
import os, time

def input_check():
    while True:
        try:
            number = int(input())
            if number <= 5 and number >= 1:
                return number
            print("Number must be in [1, 5]. Try again: ", end='')
        except ValueError:
            print("It is not number. Try again: ", end='')

def main():
    game = Game()
    while True:
        print(f"Your current points are {game.get_points()}")
        print("Input your number (from 1 to 5): ", end='')
        user_num = input_check()
        if game.guess_the_number(user_num):
            print("You win!")
        else:
            print("You lose!")
        time.sleep(1)
        os.system('cls')


if __name__ == '__main__':
    main()