class Vehicle:
    def __init__(self) -> None:
        print("From Vehicle class.")


class Car(Vehicle):
    def __init__(self) -> None:
        print("From Car class")
        super().__init__()


class OffRoad(Car):
    def __init__(self) -> None:
        print("From Off road Class")
        super().__init__()


class CityRide(Car):
    def __init__(self) -> None:
        print("Form City Ride Class")
        super().__init__()


class SUV(OffRoad, CityRide):
    def __init__(self) -> None:
        print("From SUV Class")
        super().__init__()


suv = SUV()
