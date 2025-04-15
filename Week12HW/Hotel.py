# Define the HotelRoom class
class HotelRoom:
    def __init__(self, room_number, room_type, is_booked=False):
        self.room_number = room_number
        self.room_type = room_type
        self.is_booked = is_booked

    def BookRoom(self):
        if not self.is_booked:
            self.is_booked = True
            print(f"Room {self.room_number} has been successfully booked.")
        else:
            print(f"Room {self.room_number} is already booked.")

    def CancelBooking(self):
        if self.is_booked:
            self.is_booked = False
            print(f"Booking for Room {self.room_number} has been canceled.")
        else:
            print(f"Room {self.room_number} is not currently booked.")


# Main program
room1 = HotelRoom(101, "Single")
room2 = HotelRoom(202, "Double")

print("Welcome to the Hotel Reservation System!")
print("Available rooms:")
print(f"1. Room {room1.room_number} - {room1.room_type}")
print(f"2. Room {room2.room_number} - {room2.room_type}")
print()

choice = input("Enter 1 to book Room 101 or 2 to book Room 202: ")

if choice == "1":
    room1.BookRoom()
elif choice == "2":
    room2.BookRoom()
else:
    print("Invalid input.")

cancel_choice = input("Do you want to cancel a booking? (yes/no): ")

if cancel_choice.lower() == "yes":
    cancel_room = input("Enter 1 to cancel Room 101 or 2 to cancel Room 202: ")
    if cancel_room == "1":
        room1.CancelBooking()
    elif cancel_room == "2":
        room2.CancelBooking()
    else:
        print("Invalid input.")
