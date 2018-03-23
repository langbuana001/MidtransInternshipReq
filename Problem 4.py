#Problem 4 - Elevator Problem

from Elevator import *
from Floor import *

#The requests are at the same time.
p1 = {'orig': 1, 'dest': 5 }
p2 = {'orig': 2, 'dest': 3 }
p3 = {'orig': 2, 'dest': 4 }
p4 = {'orig': 3, 'dest': 4 }
p5 = {'orig': 3, 'dest': 1 }
p6 = {'orig': 5, 'dest': 1 }

number_of_floors = 5
requests = [p1, p2, p3, p4, p5, p6]
groupings = {}
floors = []
elevator = Elevator(number_of_floors)

#Let us create arbitrary floors
#Assume we have 5 floors
for i in range(1, number_of_floors+1):
    floors.append(Floor(i))

#Register origin requests
for i in requests:
    floors[i['orig']-1].status = True
        
#Group destination requests
for i in requests:
    for key, value in i.items():
        groupings.setdefault(key, []).append(value)

#At this point, everyone has requested the elevator
#and the elevator has their requests (While this is very unrealistic)
def elevator_run():
    #Run the elevator
    while elevator.status():
        #Check the current floor
        print("=======")
        print("destinations : ", elevator.list_of_destinations)
        print("current floor: ", elevator.current_floor)
        if (floors[elevator.current_floor - 1].request_status() or elevator.current_floor in elevator.list_of_destinations): #We have a request
            elevator.embark()
            print("Embark")
            #Clear the button when we reached a floor
            while elevator.current_floor in elevator.list_of_destinations:
                elevator.list_of_destinations.remove(elevator.current_floor)
            #Take user's floor destination
            while elevator.current_floor in groupings['orig']:
                elevator.list_of_destinations.append(groupings['dest'][0])
                del groupings['orig'][0]
                del groupings['dest'][0]
                floors[elevator.current_floor - 1].status = False    
            #Prevent the elevator from becoming Apollo 13
            if elevator.current_floor == elevator.number_of_floors:
                print("Change Direction")
                elevator.direction = 0
            #Prevent the elevator from becoming an oil drilling machine
            elif elevator.current_floor == 1:
                elevator.direction = 1
                
            #It's now safe, let's go
            if elevator.direction == 1 and len(elevator.list_of_destinations) != 0:
                elevator.go_up()
                print("Going Up!")
            elif elevator.direction == 0 and len(elevator.list_of_destinations) != 0:
                elevator.go_down()
                print("Going Down!")
            else:
                elevator.operation_status = False
            
        else: #No request at current floor
            #Check direction
            if elevator.direction == 1:
                elevator.go_up()
                print("Going Up!")
            else:
                elevator.go_down()
                print("Going Down!")
    print("=======")
    print("Operation Done")
    print("Total points: ", elevator.travel_use)

elevator_run()
                















            


    
