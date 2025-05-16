class VendingMachine:
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