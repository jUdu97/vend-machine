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

    def show_options(self):
        """ Prints options available in vending machine """
        print('-' * 70)
        print('{:<20} {:<20} {:<20}\n'.format('Oreo Pack (A1)', 'Cheez-its (A2)', 'Snickers (A3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Fudge Rounds (B1)', 'Twizzlers (B2)', 'Sour Patch Kids (B3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Skittles (C1)', 'M & Ms (C2)', 'Babe Ruth (C3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Hubba Bubba (D1)', 'Snickers (D2)', 'Slim Jim (D3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Hot Cheetos (E1)', '5 Gum (E2)', 'Animal Crackers (E3)'))
        print('-' * 70)

    def make_selection(self):
        """ """
        dict_vend_opts = {'A1': '2.00','A2': '1.00','A3': '1.00',
                          'B1': '1.75','B2': '1.50','B3': '2.25',
                          'C1': '1.50','C2': '1.25','C3': '0.50',
                          'D1': '1.25','D2': '1.75','D3': '1.75',
                          'E1': '1.00','E2': '1.25','E3': '0.75'}

        #ask user which snack they want to check price for
        choice_vend =  input("Enter snack code: ")

        #ask if that choice is what they want
        choice_confirm = input("CONFIRM (Y/N)?: ")

        #case if confirmation input is YES
        if choice_confirm.upper() == "Y":
            #make cases for each selection choice
            if choice_vend == " ":
                print("Please enter a snack code: ")
            elif choice_vend[:1].upper() == "A":
                if choice_vend[1:] == "1":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                else:
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
            elif choice_vend[:1].upper() == "B":
                if choice_vend[1:] == "1":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                else:
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
            elif choice_vend[:1].upper() == "C":
                if choice_vend[1:] == "1":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                else:
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
            elif choice_vend[:1].upper() == "D":
                if choice_vend[1:] == "1":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                else:
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
            elif choice_vend[:1].upper() == "E":
                if choice_vend[1:] == "1":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
                else:
                    print("Cost: $", dict_vend_opts[choice_vend.upper()])
            else:
                while choice_vend.upper() not in dict_vend_opts.keys():
                    print("Not a valid selection. Try again!\n")
                    choice_vend =  input("Check snack price: ")
                    if choice_vend.upper() in dict_vend_opts.keys():
                        print("Cost: ", dict_vend_opts[choice_vend.upper()])
                        break
        #case if confirmation input is NO
        elif choice_confirm.upper() == "N":
            while choice_confirm.upper() != "Y":
                #ask user which snack they want to check price for
                choice_vend =  input("Enter snack code: ")
                #ask if that choice is what they want
                choice_confirm = input("CONFIRM (Y/N)?: ")
                if choice_confirm.upper() == "Y":
                    break
        #case if confirmation input is anything other than YES or NO
        else:
            while choice_confirm.upper() != "Y" and choice_confirm.upper() != "N":
                print("Not a valid input. Try again!")
                #ask user which snack they want to check price for
                choice_vend =  input("Enter snack code: ")
                #ask if that choice is what they want
                choice_confirm = input("CONFIRM (Y/N)?: ")
                if choice_confirm.upper() == "Y" or choice_confirm.upper() == "N":
                    break
        #select which snack user confirms to buy based on price
        sel_vend = input("Select your snack: ")
        while sel_vend.upper() not in dict_vend_opts.keys():
            print("Not a valid selection. Try again!\n")
            sel_vend =  input("Check snack price: ")
            if sel_vend.upper() in dict_vend_opts.keys():
                break
        sel_price = dict_vend_opts[sel_vend.upper()]
        print('Price: ${:0.2f}'.format(float(sel_price)))

        #make list of approved amount inputs
        priceLst = []
        for i in range(100):
            priceLst.append(i*0.25)
        #ask user to pay for snack
        ask_price = input("Amount: ")
        if float(ask_price) not in priceLst:
            print("Invalid input. Use different currency.")
            while float(ask_price) not in priceLst:
                ask_price = input("Amount: ")
                if float(ask_price) in priceLst:
                    break
        userChg = float(ask_price) - float(sel_price)

        #case statements for user amount
        if float(ask_price) > float(sel_price):
            userChg = float(userChg)
            print("Change: ${:0.2f}".format(float(userChg)))
            print("\nSnack vended!\nThanks for buying!")
        elif float(ask_price) < float(sel_price):
            userChg = float(sel_price) - float(ask_price)
            userChg = float(userChg)
            newChg = float(sel_price) - float(userChg)
            while newChg != 0:
                print('You need: ${:0.2f}'.format(float(userChg)), ' to vend this snack.\nKeep going!')
                ask_price = input("Amount: ")
                newChg = float(userChg) - float(ask_price)
                userChg = float(newChg)
            print("\nSnack vended!\nThanks for buying!")
        else:
            userChg = float(userChg)
            print("\nSnack vended!\nThanks for buying!")