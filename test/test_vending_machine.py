#imports
from vending_machine import VendingMachine

#main
dict_vend_opts = {'A1': '2.00','A2': '1.00','A3': '1.00',
                  'B1': '1.75','B2': '1.50','B3': '2.25',
                  'C1': '1.50','C2': '1.25','C3': '0.50',
                  'D1': '1.25','D2': '1.75','D3': '1.75',
                  'E1': '1.00','E2': '1.25','E3': '0.75'}
vMach = VendingMachine("Lemmingway", dict_vend_opts)
vMach.print_welcome()
vMach.show_options()
vMach.make_selection()