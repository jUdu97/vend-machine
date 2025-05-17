class VendingMachine:

    dict_vend_opts = None

    def __init__(self, name):
        self.name=name

    def __str__(self):
        return f"{self.name}"

    def print_welcome(self):
        """ Prints welcome message to vending machine """
        print('Welcome to '+self.name+' Vending Machine!!\n')
        print('-' * 70)
        print('ONLY ACCEPTS QUARTERS ($0.25)!')
        print('-' * 70)

    def show_options(self):
        """ Prints options available in vending machine """
        print('-' * 70)
        print('{:<20} {:<20} {:<20}\n'.format('Oreo Pack (A1)', 'Cheez-its (A2)', 'Snickers (A3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Fudge Rounds (B1)', 'Twizzlers (B2)', 'Sour Patch Kids (B3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Skittles (C1)', 'M & Ms (C2)', 'Babe Ruth (C3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Hubba Bubba (D1)', 'Snickers (D2)', 'Slim Jim (D3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Hot Cheetos (E1)', '5 Gum (E2)', 'Animal Crackers (E3)'))
        print('-' * 70)