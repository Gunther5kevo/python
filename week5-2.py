# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Child classes with their own move() definitions
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "🚤 Sailing on water"


class Bicycle(Vehicle):
    def move(self):
        return "🚴 Pedaling along the path"


# Test polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())
