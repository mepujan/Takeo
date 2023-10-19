class Vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        ''' default fare charge of the vehicle'''
        return self.seating_capacity * 100


class Bus(Vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def fare(self):
        ''' returns the fare of bus along with 10% of maintainance charge'''
        return super().fare() + 0.1 * super().fare()


bus = Bus(50)
print("The Bus Fare is : ", bus.fare())
