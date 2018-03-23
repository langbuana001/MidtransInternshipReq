class Floor:

    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.status = False
    
    def request_status(self):
        return self.status
