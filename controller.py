from view import View as v
from tournament import Tournament as t

def main():
    view = v()
    switch_choice(view)

def switch_choice(view_object):
    view_object.list_choice()

    choice = view_object.choice

    if choice == 1:
        create_tournament()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        print("\nCe choix n'est pas dans la iste !\n")
        switch_choice(view_object)

def create_tournament():
    new_tournament = t()