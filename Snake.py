print("The GBV report hub is a python program to facilitate the reporting of gender-based violence and any other kind of violence.\n")
def mainMenu():
    print("1. Report")
    print("2. Quit")
    selection = int(input("If you want to report, type 1, and if not type 2: \n"))
    if selection == 1:
        Report()
    elif selection == 2:
        exit
    else:
        print("Invalid choice. Enter 1-2\n")
    mainMenu()

def Report():
        print("1. Yes")
        print("2. No")
        slection = int(input("Are you ready to report, type 1 if you are, and if you want to quit, type  2: \n"))
        if slection == 1:
            Data()
        elif slection == 2:
            exit
        else:
            print("Invalid choice. Enter 1-2. \n")
            Report()

def Data():
    n = str(input("Waht is your name ?\n"))
    
    if n.isalpha():
        print("Your name is " + n + ".\n")
        Age()
    else:
        print("Invalid name. Retry again: \n")
        Data()

def Age():
    n1 = input("How old are you? \n")

    if n1.isdigit():
        print("You are " + n1 + " years old.\n")
        Gender()
    else:
        print("Invalid age. Please retry again: \n")
        Age()

def Gender():
    print("1. Male")
    print("2. Female")
    n2 = int(input("What is your gender? \n"))
    if n2 == 1:
        print("You are male. \n")
        Phonenumber()
    elif n2 == 2:
        print("You are female. \n")
        Phonenumber()
    else:
        print("Invalid: enter 1 or 2: \n")
        Gender()

def Phonenumber():
    n3 = input("Enter your phonr number: \n")
    if len(n3) == 10:
        print("Your phone number is: " + n3 + "\n")
        Location()
    elif n3.isalpha():
        print("Error. Retry again: \n")
        Phonenumber() 
    else:
        print("Error. Retry again: \n")
        Phonenumber()

def Location():
    n4 = str(input("Enter your province:\n"))
    if n4.isalpha():
        print("Province: " + n4 + "\n")
        District()
    else:
        print("Invalid. Retry again: \n")
        Location()
    
def District():

        n5 = str(input("Enter your Distric: \n"))
        if n5.isalpha():
            print("Your District is: " + n5 + "\n")
            Sector()
        else:
            print("Invalid. Retry again:\n")
            District()
    
def Sector():

        n6 = str(input("Enter your sector:\n"))
        if n6.isalpha():
            print("Your sector is " + n6 + "\n")
            Explain()
        else:
            print("Invali. Retry again:")
            Sector()

def Explain():
    n7 = str(input("Explain briefly your case in at least 50 words:\n\n\n\n"))
    if len(n7) < 50:
        print(" At least 50 words!!!")
        Explain()
    else:
        print(n7)
        CCL()

def CCL():
    print("Thanks For reporting your case.\n\n")
    print("1. Main manu")
    print("2. Exit")
    n8 = int(input("If you want go back to the main menu, type 1, and if you want to quit, type 2:\n"))
    if n8 == 1:
        mainMenu()
    elif n8 == 2:
        exit
    else:
        print("Please choose 1 or 2")
        CCL()



    


mainMenu()