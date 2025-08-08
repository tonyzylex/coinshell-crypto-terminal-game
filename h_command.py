import os

def show_help():
    os.system('cls' if os.name == 'nt' else 'clear')

    help_info = """
Welcome to Coin$hell

As you might have observed, the tool is exculsively for the VSCode terminal to make 
trading experience as straightforward as possible.  There's not much to learn—simply 
click or type. Go on ahead and gambl— trade!
"""
    print(help_info)

    while True:
        back_command = input("(b) to go back >> ").strip().lower()
        if back_command == 'b':
            os.system('cls' if os.name == 'nt' else 'clear')
            return 'back'
        else:
            print("Invalid input. Press 'b' to go back.")
