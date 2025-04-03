class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

def main():
    # The vehicle type is hard-coded as "car"
    vehicle_type = "car"
    
    # Ask for user input for each attribute
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    
    # Validate the input for doors: should be 2 or 4.
    while True:
        doors = input("Enter the number of doors (2 or 4): ")
        if doors in ['2', '4']:
            break
        print("Invalid entry. Please enter either 2 or 4.")
    
    roof = input("Enter the type of roof (solid or sun roof): ")
    
    # Create an Automobile instance using the user inputs
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    # Output the collected data in a formatted manner
    print("\nHere is the information you entered:")
    car.display_info()

if __name__ == "__main__":
    main()
