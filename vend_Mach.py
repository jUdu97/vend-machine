def vendM():
    """give user options  for virtual vending machine"""

    #print options for vending machine
    print('{:<20} {:<20} {:<20}\n'.format('Oreo Pack (A1)', 'Cheez-its (A2)', 'Snickers (A3)'))
    print('{:<20} {:<20} {:<20}\n'.format('Fudge Rounds (B1)', 'Twizzlers (B2)', 'Sour Patch Kids (B3)'))
    print('{:<20} {:<20} {:<20}\n'.format('Skittles (C1)', 'M & Ms (C2)', 'Babe Ruth (C3)'))
    print('{:<20} {:<20} {:<20}\n'.format('Hubba Bubba (D1)', 'Snickers (D2)', 'Slim Jim (D3)'))
    print('{:<20} {:<20} {:<20}\n'.format('Hot Cheetos (E1)', '5 Gum (E2)', 'Animal Crackers (E3)'))

    #dictionary of vending option codes and prices
    dict_vend_opts = {'A1':'$2.00','A2':'$1.15','A3':'$1.00',
                      'B1':'$1.85','B2':'$1.50','B3':'$2.00',
                      'C1':'$1.50','C2':'$1.35','C3':'$0.85',
                      'D1':'$1.35','D2':'$1.65','D3':'$1.75',
                      'E1':'$1.00','E2':'$1.25','E3':'$0.95'}

    #ask user which snack they want to check price for
    choice_vend =  input("Check snack price: ")
    #make cases for each selection
    if choice_vend == " ":
        print("Please enter a snack code: ")
    elif choice_vend[:1] == "A":
        if choice_vend[1:] == "1":
            print("Cost: ", dict_vend_opts[choice_vend])
        elif choice_vend[1:] == "2":
            print("Cost: ", dict_vend_opts[choice_vend])
        else:
            print("Cost: ", dict_vend_opts[choice_vend])
    elif choice_vend[:1] == "B":
        if choice_vend[1:] == "1":
            print("Cost: ", dict_vend_opts[choice_vend])
        elif choice_vend[1:] == "2":
            print("Cost: ", dict_vend_opts[choice_vend])
        else:
            print("Cost: ", dict_vend_opts[choice_vend])
    elif choice_vend[:1] == "C":
        if choice_vend[1:] == "1":
            print("Cost: ", dict_vend_opts[choice_vend])
        elif choice_vend[1:] == "2":
            print("Cost: ", dict_vend_opts[choice_vend])
        else:
            print("Cost: ", dict_vend_opts[choice_vend])
    elif choice_vend[:1] == "D":
        if choice_vend[1:] == "1":
            print("Cost: ", dict_vend_opts[choice_vend])
        elif choice_vend[1:] == "2":
            print("Cost: ", dict_vend_opts[choice_vend])
        else:
            print("Cost: ", dict_vend_opts[choice_vend])
    elif choice_vend[:1] == "E":
        if choice_vend[1:] == "1":
            print("Cost: ", dict_vend_opts[choice_vend])
        elif choice_vend[1:] == "2":
            print("Cost: ", dict_vend_opts[choice_vend])
        else:
            print("Cost: ", dict_vend_opts[choice_vend])
    else:
        while choice_vend not in dict_vend_opts.keys():
            print("Not a valid selection. Try again!\n")
            choice_vend =  input("Check snack price: ")
            if choice_vend in dict_vend_opts.keys():
                print("Cost: ", dict_vend_opts[choice_vend])

    #select which snack based on price
    sel_vend = input("Select your snack: ")
    print("Price: ", dict_vend_opts[sel_vend])
            
    return None
