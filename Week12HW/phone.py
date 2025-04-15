# Define the MobilePhone class
class MobilePhone:
    def __init__(self, brand, model, storage_capacity, price):
        self.brand = brand
        self.model = model
        self.storage_capacity = storage_capacity
        self.price = price

    def DisplayPhoneDetails(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage_capacity} GB")
        print(f"Price: ${self.price}")
        print("---------------------------")


# Main program
phone1 = MobilePhone("Samsung", "Galaxy S24", 128, 999)
phone2 = MobilePhone("Apple", "iPhone 15", 256, 1199)

phone1.DisplayPhoneDetails()
phone2.DisplayPhoneDetails()
