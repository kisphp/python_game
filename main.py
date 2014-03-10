import sys

class Main():
    max_width = 5
    max_height = 5
    character_alive = True
    character_won = False
    monster_awake = False
    monster_awakened = False
    monster_move_per_turn = 2

    def __init__(self):
        #self.display_menu()
        pass

    def display_menu(self):
        menu_list = ['Start New Game', '[Save Game]', '[Load Game]', 'Customize Setup', 'Exit']
        print('Type the number of choice')
        print()
        for i in range(1,len(menu_list) + 1):
            print(str(i) + " " + menu_list[i - 1])
        choice = input('Your Choice: ')
        self.menu_choice(choice)

    def menu_choice(self, choice):
        try:
            choice = int(choice)
        except ValueError:
            choice = 0
        if (choice == 1):
            pass
        elif (choice == 2):
            pass
        elif (choice == 3):
            pass
        elif (choice == 4):
            pass
        elif (choice == 5):
            sys.exit(0)
        else:
            print('This wasn\'t a valid option. Try again')
            self.display_menu()

    def draw_grid(self):
        height = self.max_height
        width = self.max_width

        for y in range(0, height):
            for x in range(0, width):
                y = str(y)
                x = str(x)
                sys.stdout.write('?')
            sys.stdout.write('\n')

monster = Main()
monster.draw_grid()

