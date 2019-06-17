def vendM():
    """give user options  for virtual vending machine"""

    #print options for vending machine
    print('Lemmingway Vending Machine\n')
    print('-' * 70)
    print('{:<20} {:<20} {:<20}\n'.format('Oreo Pack (A1)', 'Cheez-its (A2)', 'Snickers (A3)'))
    print('{:<20} {:<20} {:<20}\n'.format('Fudge Rounds (B1)', 'Twizzlers (B2)', 'Sour Patch Kids (B3)'))
    print('{:<20} {:<20} {:<20}\n'.format('Skittles (C1)', 'M & Ms (C2)', 'Babe Ruth (C3)'))
    print('{:<20} {:<20} {:<20}\n'.format('Hubba Bubba (D1)', 'Snickers (D2)', 'Slim Jim (D3)'))
    print('{:<20} {:<20} {:<20}\n'.format('Hot Cheetos (E1)', '5 Gum (E2)', 'Animal Crackers (E3)'))
    print('-' * 70)
    
    #dictionary of vending option codes and prices
    dict_vend_opts = {'A1': '2.00','A2': '1.00','A3': '1.00',
                      'B1': '1.75','B2': '1.50','B3': '2.25',
                      'C1': '1.50','C2': '1.25','C3': '0.50',
                      'D1': '1.25','D2': '1.75','D3': '1.75',
                      'E1': '1.00','E2': '1.25','E3': '0.75'}

    #ask user which snack they want to check price for
    choice_vend =  input("Check snack price: ")
    
    #make cases for each selection
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

    #select which snack based on price
    sel_vend = input("Select your snack: ")
    sel_price = dict_vend_opts[sel_vend.upper()]
    print('Price: ${:0.2f}'.format(float(sel_price)))

    #ask user to pay for snack
    ask_price = input("Amount: ")

    userChg = float(ask_price) - float(sel_price)

    #case statements for user amount
    if float(ask_price) > float(sel_price):
        userChg = float(userChg)
        print("Change: $", userChg)
        print("\nSnack vended!\nThanks for buying!")
    elif float(ask_price) < float(sel_price):

        userChg = float(sel_price) - float(ask_price)
        userChg = float(userChg)
        newChg = float(sel_price) - float(userChg)
        while newChg != 0:
            print('You need: ${:0.2f}'.format(float(userChg)), ' to vend this snack.\nTry again!')
            ask_price = input("Amount: ")
            newChg = float(userChg) - float(ask_price)
            userChg = float(newChg)
        print("\nSnack vended!\nThanks for buying!")
    else:
        userChg = float(userChg)
        print("\nSnack vended!\nThanks for buying!")
    
            
    return None

#https://pyformat.info/
