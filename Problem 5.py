#Problem 5 - BigO analysis
'''
    Note: Some unclarity on the prompt regarding what kind of list can we expect.
    It is stated that given A list of arrival and departure. This is ambiguous,
    can we expect that there's some sort of pattern for our schedule? It is unclear.

    As multiple correspondece for clarity was not responded, we can only assume.
'''

#Let us assume the list has an alternating time (Arrival then Departure).
arrival_and_departure2 = [1000, 1005, 1005, 1015, 1010, 1030, 1025, 1040, 1045, 1050]
number_of_bus2 = 5

#Uncomment the below code for interactive mode
'''
arrival_and_departure = []
number_of_bus = int(input("Enter number of bus :"))

for i in range(0, number_of_bus):
    print("Bus number ", i+1)
    arrival_and_departure.append(int(input("Arrival Time   :")))
    arrival_and_departure.append(int(input("Departure Time :")))
    print("")
'''

def max_number(arrival_and_departure_list, no_of_bus):
    max_number = 0
    for i in range(0, no_of_bus):   #O(n) as it grows linearly
        #Realistically, busses don't leave the station at the exact time
        #Even if it does, it should take about 1-2 minutes for it to leave
        #   the building. Hence the "bigger or equal to" comparison
        if arrival_and_departure_list[i+1] >= arrival_and_departure_list[i+2]:  
            max_number += 1     #O(constant) as this is a simple addition
    return max_number

print("The maximum amount of bus at one time was",max_number(arrival_and_departure2, number_of_bus2), "busses")

#max_number has only one 'for' loop.
#Thus the BigO should be O(n)

