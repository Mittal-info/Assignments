"""


parking_system.py
│
├── Vehicle (Parent Class)
│   └── parking_charge()
│
├── TwoWheeler (Child of Vehicle)
│
├── FourWheeler (Child of Vehicle)
│   └── ElectricCar (Child of FourWheeler)
│
├── ValetService (Plain Class)
│   └── valet_fee()
│
├── ValetElectricCar
│   ├── Inherits ElectricCar
│   ├── Inherits ValetService
│   └── bill()
│
└── Day-End Report
    ├── List of 8 vehicles
    └── Total Parking Revenue


"""


# Parent Class

class Vehicle:

    def __init__(self, reg_no, owner, hours, rate):
        self.reg_no = reg_no
        self.owner = owner
        self.hours = hours
        self.rate = rate

    def parking_charge(self):
        return self.hours * self.rate


# Child Class - Two Wheeler

class TwoWheeler(Vehicle):

    def __init__(self, reg_no, owner, hours):
        super().__init__(reg_no, owner, hours, 10)


# Child Class - Four Wheeler

class FourWheeler(Vehicle):

    def __init__(self, reg_no, owner, hours):
        super().__init__(reg_no, owner, hours, 30)


# Electric Car inherits FourWheeler

class ElectricCar(FourWheeler):

    def __init__(self, reg_no, owner, hours, battery_kwh):
        super().__init__(reg_no, owner, hours)
        self.battery_kwh = battery_kwh

    def charging_cost(self, units):
        return units * 12


# Plain Class - Valet Service

class ValetService:

    def valet_fee(self):
        return 50


# Multiple Inheritance

class ValetElectricCar(ElectricCar, ValetService):

    def __init__(self, reg_no, owner, hours, battery_kwh):
        ElectricCar.__init__(self, reg_no, owner, hours, battery_kwh)

    def bill(self, units):
        return (
            self.parking_charge()
            + self.charging_cost(units)
            + self.valet_fee()
        )


# Testing Question 1

four = FourWheeler("GJ01AB1234", "Rahul", 3)
two = TwoWheeler("GJ01CD5678", "Amit", 5)

print("Four Wheeler Parking:", four.parking_charge())
print("Two Wheeler Parking:", two.parking_charge())


# Testing Question 2

electric = ElectricCar("GJ01EF1234", "Priya", 2, 60)

print("Electric Car Parking:", electric.parking_charge())
print("Charging Cost:", electric.charging_cost(10))


# Testing Question 3

valet_car = ValetElectricCar("GJ01GH5678", "Neha", 2, 75)

print("Valet Electric Car Bill:", valet_car.bill(10))


# Question 4 - Day End Report

vehicles = [

    Vehicle("GJ01AA1111", "A", 2, 20),

    TwoWheeler("GJ01BB2222", "B", 3),

    TwoWheeler("GJ01CC3333", "C", 4),

    FourWheeler("GJ01DD4444", "D", 2),

    FourWheeler("GJ01EE5555", "E", 3),

    ElectricCar("GJ01FF6666", "F", 2, 60),

    ElectricCar("GJ01GG7777", "G", 4, 80),

    ValetElectricCar("GJ01HH8888", "H", 2, 75)

]


total_revenue = 0

print("\n========== DAY END REPORT ==========")

for vehicle in vehicles:

    print("Class:", type(vehicle).__name__)
    print("Registration No:", vehicle.reg_no)
    print("Parking Charge: ₹", vehicle.parking_charge())
    print("--------------------------------")

    total_revenue += vehicle.parking_charge()


print("Total Parking Revenue: ₹", total_revenue)
