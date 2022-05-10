import random

from pkg_resources import ResolutionError


def play():
    user = input(f"enter a choice ")
    comp = random.choice(['r', 'p', 's'])

    if is_win(user, comp):
        print("you won")

    else:
        print("you lose")


def is_win(player, computer):
    if(player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True


play()
