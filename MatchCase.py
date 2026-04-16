a = int(input("Enter a no: "))

match a: # Like a switch statement
    case 1:
        print("Case 1")
    case 2:
        print("Case 2")
    case 13:
        print("Case 13")
    case _:
        print("No Case Found")