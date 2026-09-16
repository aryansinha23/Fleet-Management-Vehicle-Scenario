"""
Task 2 : Fleet Management (Vehicle)  -- Python version of FleetManagement.java
Tracks fuel level, mileage and range for a transport company's vehicles.

Run:  python fleet.py
"""


class Vehicle:
    """A single vehicle in the fleet."""

    def __init__(self, make: str, model: str, fuel_level: float, mileage: float):
        self.make = make                # manufacturer, e.g. "Maruti"
        self.model = model              # model name,   e.g. "Swift"
        self.fuel_level = float(fuel_level)   # litres in the tank
        self.mileage = float(mileage)         # km per litre

    # ---------- helpers ----------
    def label(self) -> str:
        return f"{self.make} {self.model}"

    def get_range(self) -> float:
        return self.fuel_level * self.mileage

    # ---------- behaviour ----------
    def drive(self, distance: float) -> bool:
        """Attempt a trip of `distance` km. Returns True if the trip happened."""
        if distance <= 0:
            print(f"[{self.label()}] Distance must be greater than 0 km.")
            return False

        fuel_needed = distance / self.mileage

        if fuel_needed <= self.fuel_level:
            self.fuel_level -= fuel_needed
            print(f"[{self.label()}] Trip done: {distance:.1f} km | "
                  f"fuel used {fuel_needed:.2f} L | fuel left {self.fuel_level:.2f} L")
            return True

        shortfall = fuel_needed - self.fuel_level
        print(f"[{self.label()}] Not enough fuel: needs {fuel_needed:.2f} L, "
              f"has {self.fuel_level:.2f} L (short by {shortfall:.2f} L)")
        return False

    def refuel(self, liters: float) -> bool:
        """Add fuel to the tank."""
        if liters <= 0:
            print(f"[{self.label()}] Refuel amount must be greater than 0 L.")
            return False
        self.fuel_level += liters
        print(f"[{self.label()}] Refuelled {liters:.2f} L | tank now {self.fuel_level:.2f} L")
        return True

    def check_range(self) -> float:
        """Print and return the distance still available on the current tank."""
        r = self.get_range()
        print(f"[{self.label()}] Range: {r:.1f} km on {self.fuel_level:.2f} L "
              f"at {self.mileage:.1f} km/L")
        return r


def main():
    print("===== FleetOps : Vehicle Console =====\n")

    compact = Vehicle("Maruti", "Swift", 12.0, 21.5)       # compact car
    truck = Vehicle("Tata", "LPT 1618", 60.0, 4.2)         # delivery truck

    print("-- Starting condition --")
    compact.check_range()
    truck.check_range()

    print("\n-- Trips --")
    compact.drive(180)     # comfortably possible
    truck.drive(400)       # needs ~95 L, tank holds 60 L -> fails

    print("\n-- Refuelling the truck --")
    truck.refuel(50)
    truck.drive(400)       # retry the same trip

    print("\n-- Range comparison --")
    compact.check_range()
    truck.check_range()

    further = compact if compact.get_range() >= truck.get_range() else truck
    print(f"\nFurthest on current fuel: {further.label()} ({further.get_range():.1f} km)")


if __name__ == "__main__":
    main()
