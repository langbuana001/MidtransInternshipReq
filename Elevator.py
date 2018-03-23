class Elevator:

    def __init__(self, number):
        self.number_of_floors = number #We hard code no. of floors for efficiency
        self.travel_use = 0 #Whoaa brand new!
        self.current_floor = 1 #Starts at 1
        self.operation_status = True
        self.list_of_destinations = []
        self.direction = 1 #1 for up, 0 for down

    def status(self):
        return self.operation_status

    def go_up(self):
        self.travel_use += 1
        self.current_floor += 1

    def go_down(self):
        self.travel_use += 1
        self.current_floor -= 1

    def embark(self):
        self.travel_use += 2
        if self.current_floor in self.list_of_destinations:
            self.list_of_destinations.remove(self.current_floor)

    def add_floor_destination(self, x):
        self.list_of_destinations.append(x)
    
