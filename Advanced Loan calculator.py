import time

amt = 0
rat = 0
yer = 0
ni = 0

print ("Welcome to Cyclops bank!")
print ("")
time.sleep(1)
print(r"""
    ----------------------------------------------------------------
     _______           _______  _        _______  _______  _______   
    (  ____ \|\     /|(  ____ \( \      (  ___  )(  ____ )(  ____ \  
    | (    \/( \   / )| (    \/| (      | (   ) || (    )|| (    \/  
    | |       \ (_) / | |      | |      | |   | || (____)|| (_____   
    | |        \   /  | |      | |      | |   | ||  _____)(_____  )  
    | |         ) (   | |      | |      | |   | || (            ) |  
    | (____/\   | |   | (____/\| (____/\| (___) || )      /\____) |  
    (_______/   \_/   (_______/(_______/(_______)|/       \_______)

    ----------------------------------------------------------------
                                                                """)
time.sleep(1)

print ("Let's calculate Your loan....")
print ("")
time.sleep(1)


x = int(input("1. Home loan \n2. Car loan \n3. Student loan \n4. Personal loan \n5. Exit \n>>> "))
print ("")


if x == 1:
    y = int(input("1. Simple intrest \n2. Compound intrest \n>>> "))
    if y == 1:
        print ("Intrest rate on Home loan is 6%")
        amt = eval(input("Enter your loan amount ($): "))
        yer = eval(input("Estimted time for payback of loan (Years): " ))

        tot = amt * 6 * yer
        print ("Your monthly payment will be :",tot)

    if y == 2:
        print ("Intrest rate on Home loan is 6%")
        amt = eval(input("Enter your loan amount ($): "))
        ni = eval(input("Number of times the intrest is to be compounded(annually):"))
        yer = eval(input("Estimted time for payback of loan (Years): " ))

        tot = amt * 1 + 6 / ni * yer
        print ("Your monthly payment will be :",tot)


if x == 2:
    y = int(input("1. Simple intrest \n2. Compound intrest \n>>> "))
    if y == 1:
        print ("Intrest rate on Car loan is 10%")
        amt = eval(input("Enter your loan amount ($): "))
        yer = eval(input("Estimted time for payback of loan (Years): " ))

        tot = amt * 10 * yer
        print ("Your monthly payment will be :",tot)

    if y == 2:
        print ("Intrest rate on Car loan is 10%")
        amt = eval(input("Enter your loan amount ($): "))
        ni = eval(input("Number of times the intrest is to be compounded(annually):"))
        yer = eval(input("Estimted time for payback of loan (Years): " ))

        tot = amt * 1 + 10 / ni * yer
        print ("Your monthly payment will be :",tot)

if x == 3:
    y = int(input("1. Simple intrest \n2. Compound intrest \n>>> "))
    if y == 1:
        print ("Intrest rate on Student loan is 5%")
        amt = eval(input("Enter your loan amount ($): "))
        yer = eval(input("Estimted time for payback of loan (Years): " ))

        tot = amt * 5 * yer
        print ("Your monthly payment will be :",tot)

    if y == 2:
        print ("Intrest rate on Student loan is 5%")
        amt = eval(input("Enter your loan amount ($): "))
        ni = eval(input("Number of times the intrest is to be compounded(annually):"))
        yer = eval(input("Estimted time for payback of loan (Years): " ))

        tot = amt * 1 + 5 / ni * yer
        print ("Your monthly payment will be :",tot)

if x == 4:
    y = int(input("1. Simple intrest \n2. Compound intrest \n>>> "))
    if y == 1:
        print ("Intrest rate on Personal loan is 13%")
        amt = eval(input("Enter your loan amount ($): "))
        yer = eval(input("Estimted time for payback of loan (Years): " ))

        tot = amt * 13 * yer
        print ("Your monthly payment will be :",tot)

    if y == 2:
        print ("Intrest rate on Personal loan is 13%")
        amt = eval(input("Enter your loan amount ($): "))
        ni = eval(input("Number of times the intrest is to be compounded(annually):"))
        yer = eval(input("Estimted time for payback of loan (Years): " ))

        tot = amt * 1 + 13 / ni * yer
        print ("Your monthly payment will be :",tot)

if x == 5:
    print ("Have a good day!")
    exit()
    