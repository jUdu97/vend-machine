def vendM():
    """give user options  for virtual vending machine"""

    #print options for vending machine
    print('Oreo Pack {0:10} Cheez-its {1:10} Snickers {2:10}\n'.format('(A1)', '(A2)', '(A3)'))
    print("Fudge Rounds (B1)\t\tTwizzlers (B2)\tSour Patch Kids (B3)\n")
    print("Skittles (C1)\t\tM & Ms (C2)\t\tBabe Ruth (C3)\n")
    print("Hubba Bubba Max (D1)\tSnickers (D2)\tSlim Jim (D3)\n")
    print("Hot Cheetos (E1)\t\t5 Gum (E2)\t\tAnimal Crackers (E3)\n")

    #dictionary of vending option codes and prices
    dict_vend_opts = {'A1':'$2.00','A2':'$1.15','A3':'$1.00',
                      'B1':'$1.85','B2':'$1.50','B3':'$2.00',
                      'C1':'$1.50','C2':'$1.35','C3':'$0.85',
                      'D1':'$1.35','D2':'$1.65','D3':'$1.75',
                      'E1':'$1.00','E2':'$1.25','E3':'$0.95'}
    #ask user for their choice
    choice_vend =  input("Select your snack: ")

    #make cases for each selection
    if choice_vend == " ":
        pass
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
            print("Not a selection. Try again!\n")
            choice_vend =  input("Select your snack: ")
            if choice_vend in dict_vend_opts.keys():
                print("Cost: ", dict_vend_opts[choice_vend])
            
    return None
