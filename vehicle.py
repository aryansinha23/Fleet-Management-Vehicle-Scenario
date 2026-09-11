class Vehicle:
    def __init__(self, make, model, fuel_level, mileage):
        self.make = make
        self.model = model
        self.fuel_level = fuel_level      # in liters
        self.mileage = mileage            # in km/l

    def drive(self, distance):
        fuel_needed = distance / self.mileage
        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"{self.make} {self.model}: Trip of {distance} km completed. "
                  f"Fuel used: {fuel_needed:.2f} L. Remaining fuel: {self.fuel_level:.2f} L")
        else:
            print(f"{self.make} {self.model}: Not enough fuel for a {distance} km trip! "
                  f"Needed {fuel_needed:.2f} L but only {self.fuel_level:.2f} L available.")

    def refuel(self, liters):
        if liters <= 0:
            print(f"{self.make} {self.model}: Refuel amount must be positive.")
            return
        self.fuel_level += liters
        print(f"{self.make} {self.model}: Refueled {liters:.2f} L. "
              f"Current fuel level: {self.fuel_level:.2f} L")

    def check_range(self):
        range_km = self.fuel_level * self.mileage
        print(f"{self.make} {self.model}: Current range is {range_km:.2f} km "
              f"(fuel: {self.fuel_level:.2f} L, mileage: {self.mileage:.2f} km/l)")
        return range_km


def main():
    # Two vehicles with very different specs
    compact_car = Vehicle("Maruti Suzuki", "Swift", fuel_level=30.0, mileage=22.0)   # compact car
    delivery_truck = Vehicle("Tata", "407", fuel_level=80.0, mileage=6.0)            # heavy delivery truck

    print("=== Initial Ranges ===")
    compact_car.check_range()
    delivery_truck.check_range()

    print("\n=== Attempting Trips ===")
    compact_car.drive(300)          # should succeed easily
    delivery_truck.drive(600)       # needs 100 L, only has 80 L -> should fail

    print("\n=== Refueling the Truck ===")
    delivery_truck.refuel(50)
    delivery_truck.drive(600)       # now needs 100 L, has 130 L -> should succeed

    print("\n=== Final Range Comparison ===")
    car_range = compact_car.check_range()
    truck_range = delivery_truck.check_range()

    if car_range > truck_range:
        print(f"\nThe {compact_car.make} {compact_car.model} has the greater range "
              f"by {car_range - truck_range:.2f} km.")
    elif truck_range > car_range:
        print(f"\nThe {delivery_truck.make} {delivery_truck.model} has the greater range "
              f"by {truck_range - car_range:.2f} km.")
    else:
        print("\nBoth vehicles have the same range.")


if __name__ == "__main__":
    main()
