# class to store info about an airline flight
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # adding a method to the class. Always needs self as the first parameter
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(3)

people = ["bob", "joe", "shayan", "shrek"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"added {person} successfully")
    else:
        print(f"No space available for {person}")
