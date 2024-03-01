#write a program to calculate electricity bill in TamilNadu

name=input("Enter your name:")
print("1.Calculate for low tension supply\n2.Calculate for high tension supply")
option=int(input("Enter your option: "))
units=float(input("Enter your no of units: "))
arrayofunits = [0, 100, 200, 400, 500, 600, 800, 1000]
energy_charges_per_unit = [0, 2.25, 4.50, 6.00, 8.00, 9.00, 10.00, 11.00]
if option==1:
    print("****Low dension supply****")
    fixed_charges_for_two_months = 0
    fixed_charges_for_two_months_after_Govt_subsity = 0
    if(units >arrayofunits[0] and units <= arrayofunits[4]):
        print("Consumption upto 500 units 2 monthly")
        if(units > arrayofunits[0] and units <= arrayofunits[1]):
            bill=energy_charges_per_unit[0]
            print("Upto 100 units free scheme")

        elif(units <= arrayofunits[2]):
            bill=(100*0)+(units-100)*energy_charges_per_unit[1]

        elif(units <= arrayofunits[3]):
            bill=(100*0)+(100*2.25)+(units-200)*energy_charges_per_unit[2]

        else:
            bill=(100*0)+(100*2.25)+(200*4.50)+(units-400)*energy_charges_per_unit[3]

    elif(units > arrayofunits[4]):
        print("Consumption above 500 units 2 monthly")
        if(units > arrayofunits[0] and units <= arrayofunits[1]):
            bill=energy_charges_per_unit[0]
            print("Upto 100 units free scheme") 

        elif(units > arrayofunits[1] and units <= arrayofunits[3]):
            bill=(100*0)+(units-100)*energy_charges_per_unit[2]

        elif(units <= arrayofunits[4]):
            bill=(100*0)+(400-100)*4.50+(units-400)*energy_charges_per_unit[3]

        elif(units <= arrayofunits[5]):
            bill=(100*0)+(400-100)*4.50+(500-400)*6.00+(units-500)*energy_charges_per_unit[4]

        elif(units <= arrayofunits[6]):
            bill=(100*0)+(400-100)*4.50+(500-400)*6.00+(600-500)*8.00+(units-600)*energy_charges_per_unit[5]

        elif(units <=arrayofunits[7]):
            bill=(100*0)+(400-100)*4.50+(500-400)*6.00+(600-500)*8.00+(800-600)*9.00+(units-800)*energy_charges_per_unit[6]

        else:
            bill=(100*0)+(400-100)*4.50+(500-400)*6.00+(600-500)*8.00+(800-600)*9.00+(1000-800)*10.00+(units-1000)*energy_charges_per_unit[7]
        
elif(option==2):
    print("****High dension supply****")
    demand_charges_per_month=550
    month=int(input("How many month bill pay?"))
    print("1.Factories, Information Technology services, Industries")
    print("2.Govt.Educational Institutions, Govt.Hospitals, Railway Traction, CMRL, Lift Irrigation Societies")
    print("3.Private Educational Institutions & its hostels, Segregated Medical colleges")
    print("4.Construction activities and other Temporary purposes")
    print("5.Miscellaneous categories")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        energy_charges_per_unit=6.75

    elif(choice==2):
        energy_charges_per_unit=7.00

    elif(choice==3):
        energy_charges_per_unit=7.50

    elif(choice==4):
        energy_charges_per_unit=12.00

    elif(choice==5):
        energy_charges_per_unit=8.50

    else:
        print("Plz enter correct choice")

    bill=(units*energy_charges_per_unit)+(demand_charges_per_month*month)
print("Name:",name)
print("Your usage units:",units)
print("Total Electricity bill amount=",bill)












        

    
