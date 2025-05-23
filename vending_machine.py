class VendingMachine:
    def __init__(self, name, dictionary):
        self.name=name
        self.dictionary=dictionary

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
        print('{:<20} {:<20} {:<20}\n'.format('Oreo Pack (A1)', 'Cheez-its (A2)', 'Snickers (A3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Fudge Rounds (B1)', 'Twizzlers (B2)', 'Sour Patch Kids (B3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Skittles (C1)', 'M & Ms (C2)', 'Babe Ruth (C3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Hubba Bubba (D1)', 'Snickers (D2)', 'Slim Jim (D3)'))
        print('{:<20} {:<20} {:<20}\n'.format('Hot Cheetos (E1)', '5 Gum (E2)', 'Animal Crackers (E3)'))
        print('-' * 70)

    def __check_choice(self):
        """ Request that user select a corresponding snack code to the snack that they wish to purchase """
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
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                else:
                    print("Cost: $", self.dictionary[choice_vend.upper()])
            elif choice_vend[:1].upper() == "B":
                if choice_vend[1:] == "1":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                else:
                    print("Cost: $", self.dictionary[choice_vend.upper()])
            elif choice_vend[:1].upper() == "C":
                if choice_vend[1:] == "1":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                else:
                    print("Cost: $", self.dictionary[choice_vend.upper()])
            elif choice_vend[:1].upper() == "D":
                if choice_vend[1:] == "1":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                else:
                    print("Cost: $", self.dictionary[choice_vend.upper()])
            elif choice_vend[:1].upper() == "E":
                if choice_vend[1:] == "1":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                elif choice_vend[1:] == "2":
                    print("Cost: $", self.dictionary[choice_vend.upper()])
                else:
                    print("Cost: $", self.dictionary[choice_vend.upper()])
            else:
                while choice_vend.upper() not in self.dictionary.keys():
                    print("Not a valid selection. Try again!\n")
                    choice_vend =  input("Check snack price: ")
                    if choice_vend.upper() in self.dictionary.keys():
                        print("Cost: ", self.dictionary[choice_vend.upper()])
                        break
        #case if confirmation input is NO
        elif choice_confirm.upper() == "N":
            while choice_confirm.upper() != "Y":
                #ask if that choice is what they want
                choice_confirm = input("CONFIRM (Y/N)?: ")
                if choice_confirm.upper() == "Y":
                    break
        #case if confirmation input is anything other than YES or NO
        else:
            while choice_confirm.upper() != "Y" and choice_confirm.upper() != "N":
                print("Not a valid input. Try again!")
                #ask if that choice is what they want
                choice_confirm = input("CONFIRM (Y/N)?: ")
                if choice_confirm.upper() == "Y" or choice_confirm.upper() == "N":
                    break

    def __format_change(self, name_of_currency, price_to_convert):
        """ Formatter for prices of snacks """
        return name_of_currency+': ${:0.2f}'.format(float(price_to_convert))

    def make_selection(self):
        """ Process of making selection of snack"""
        #check choice made by user
        self.__check_choice()

        #select which snack user confirms to buy based on price
        sel_vend = input("Select your snack: ")
        if sel_vend.upper() not in self.dictionary.keys():
            while sel_vend.upper() not in self.dictionary.keys():
                print("Not a valid selection. Try again!\n")
                sel_vend =  input("Check snack price: ")
                if sel_vend.upper() in self.dictionary.keys():
                    break
        sel_price = self.dictionary[sel_vend.upper()]
        print(self.__format_change("Price", sel_price))

        #make list of approved amount inputs
        price_list = []
        for i in range(100):
            price_list.append(i*0.25)

        #ask user to pay for snack
        print('INPUT AMOUNT WITH THE FOLLOWING FORMAT: $X.XX!')
        print('-' * 70)
        ask_price = input("Amount: ")
        if float(ask_price) not in price_list:
            print("Invalid input. Use different currency.")
            while float(ask_price) not in price_list:
                ask_price = input("Amount: ")
                if float(ask_price) in price_list:
                    break
        user_chg = float(ask_price) - float(sel_price)

        #case statements for user amount
        if float(ask_price) > float(sel_price):
            print(self.__format_change("Change", user_chg)+'\nSnack vended!\nThanks for buying!')
        elif float(ask_price) < float(sel_price):
            user_chg = float(sel_price) - float(ask_price)
            new_chg = float(sel_price) - float(user_chg)
            while new_chg != 0:
                print(self.__format_change("You need", user_chg)+' to vend this snack.\nKeep going!')
                ask_price = input("Amount: ")
                new_chg = float(user_chg) - float(ask_price)
                user_chg = new_chg
            print("\nSnack vended!\nThanks for buying!")
        else:
            print("\nSnack vended!\nThanks for buying!")

        self.print_goodbye()

    def print_goodbye(self):
        """ Prints goodbye message to vending machine """
        print('-' * 70)
        print('All Content © 2025 '+self.name+' Vending Machine. All Rights Reserved.\n')
        print('-' * 70)