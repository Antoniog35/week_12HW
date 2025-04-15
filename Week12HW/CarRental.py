# Define the Car class
class Car:
    def __init__(self, brand, model, year, is_available=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_available = is_available

    def RentCar(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.brand} {self.model} ({self.year}) has been rented.")
        else:
            print(f"{self.brand} {self.model} is already rented out.")

    def ReturnCar(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.brand} {self.model} has been returned and is now available.")
        else:
            print(f"{self.brand} {self.model} is already available.")


# Main program
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Mustang", 2021)

print("Welcome to the Car Rental System!")
print("Available cars:")
print(f"1. {car1.brand} {car1.model} ({car1.year})")
print(f"2. {car2.brand} {car2.model} ({car2.year})")
print()

choice = input("Enter 1 to rent the first car, or 2 to rent the second car: ")

if choice == "1":
    car1.RentCar()
elif choice == "2":
    car2.RentCar()
else:
    print("Invalid input.")

return_choice = input("Do you want to return a car? (yes/no): ")

if return_choice.lower() == "yes":
    return_car = input("Enter 1 to return the first car, or 2 to return the second car: ")
    if return_car == "1":
        car1.ReturnCar()
    elif return_car == "2":
        car2.ReturnCar()
    else:
        print("Invalid input.")
