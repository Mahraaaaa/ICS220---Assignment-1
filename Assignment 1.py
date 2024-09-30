# Guest Class: Represents the customer who makes reservations
class Guest:
    def __init__(self, guest_id, name, email, phone, address, nationality, dob):
        # Private attributes for Guest class
        self.__guest_id = guest_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__nationality = nationality
        self.__dob = dob

    # Getter and Setter methods to access and modify the attributes
    def get_guest_id(self):
        return self.__guest_id

    def set_guest_id(self, guest_id):
        self.__guest_id = guest_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_nationality(self):
        return self.__nationality

    def set_nationality(self, nationality):
        self.__nationality = nationality

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob


# Reservation Class: Stores details about a reservation made by a guest
class Reservation:
    def __init__(self, reservation_id, check_in_date, check_out_date, room_number, guest_id, status, num_of_nights):
        # Private attributes for Reservation class
        self.__reservation_id = reservation_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__room_number = room_number
        self.__guest_id = guest_id
        self.__status = status
        self.__num_of_nights = num_of_nights

    # Getter and Setter methods for Reservation class
    def get_reservation_id(self):
        return self.__reservation_id

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_guest_id(self):
        return self.__guest_id

    def set_guest_id(self, guest_id):
        self.__guest_id = guest_id

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_num_of_nights(self):
        return self.__num_of_nights

    def set_num_of_nights(self, num_of_nights):
        self.__num_of_nights = num_of_nights

    # Placeholder method to cancel a reservation
    def cancel_reservation(self):
        # This function will cancel the reservation and update the status
        pass


# Room Class: Stores details about the rooms in the hotel
class Room:
    def __init__(self, room_number, room_type, price_per_night, availability_status, floor_number, room_capacity,
                 amenities):
        # Private attributes for Room class
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price_per_night = price_per_night
        self.__availability_status = availability_status
        self.__floor_number = floor_number
        self.__room_capacity = room_capacity
        self.__amenities = amenities

    # Getter and Setter methods for Room class
    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    def get_room_type(self):
        return self.__room_type

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def get_price_per_night(self):
        return self.__price_per_night

    def set_price_per_night(self, price_per_night):
        self.__price_per_night = price_per_night

    def get_availability_status(self):
        return self.__availability_status

    def set_availability_status(self, availability_status):
        self.__availability_status = availability_status

    def get_floor_number(self):
        return self.__floor_number

    def set_floor_number(self, floor_number):
        self.__floor_number = floor_number

    def get_room_capacity(self):
        return self.__room_capacity

    def set_room_capacity(self, room_capacity):
        self.__room_capacity = room_capacity

    def get_amenities(self):
        return self.__amenities

    def set_amenities(self, amenities):
        self.__amenities = amenities


# Payment Class: Handles payment information related to a reservation
class Payment:
    def __init__(self, payment_id, reservation_id, payment_method, total_amount, payment_date, payment_status,
                 card_last_4_digits):
        # Private attributes for Payment class
        self.__payment_id = payment_id
        self.__reservation_id = reservation_id
        self.__payment_method = payment_method
        self.__total_amount = total_amount
        self.__payment_date = payment_date
        self.__payment_status = payment_status
        self.__card_last_4_digits = card_last_4_digits

    # Getter and Setter methods for Payment class
    def get_payment_id(self):
        return self.__payment_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_reservation_id(self):
        return self.__reservation_id

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    def get_total_amount(self):
        return self.__total_amount

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    def get_payment_date(self):
        return self.__payment_date

    def set_payment_date(self, payment_date):
        self.__payment_date = payment_date

    def get_payment_status(self):
        return self.__payment_status

    def set_payment_status(self, payment_status):
        self.__payment_status = payment_status

    def get_card_last_4_digits(self):
        return self.__card_last_4_digits

    def set_card_last_4_digits(self, card_last_4_digits):
        self.__card_last_4_digits = card_last_4_digits

    # Placeholder method to process payment
    def process_payment(self):
        # This function will process the payment for the reservation
        pass


# HotelEmployee Class: Represents employees (e.g., receptionist) working in the hotel
class HotelEmployee:
    def __init__(self, employee_id, name, role, shift, email, phone, date_of_hire):
        # Private attributes for HotelEmployee class
        self.__employee_id = employee_id
        self.__name = name
        self.__role = role
        self.__shift = shift
        self.__email = email
        self.__phone = phone
        self.__date_of_hire = date_of_hire

    # Getter and Setter methods for HotelEmployee class
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def get_shift(self):
        return self.__shift

    def set_shift(self, shift):
        self.__shift = shift

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_date_of_hire(self):
        return self.__date_of_hire

    def set_date_of_hire(self, date_of_hire):
        self.__date_of_hire = date_of_hire

    # Placeholder method for checking in a guest
    def check_in_guest(self, reservation_id):
        # This function will handle guest check-in
        pass

    # Placeholder method for checking out a guest
    def check_out_guest(self, reservation_id):
        # This function will handle guest check-out
        pass


# Hotel Class: Represents the hotel where reservations are made
class Hotel:
    def __init__(self, hotel_id, name, location, number_of_rooms, rating, amenities, contact_number):
        # Private attributes for Hotel class
        self.__hotel_id = hotel_id
        self.__name = name
        self.__location = location
        self.__number_of_rooms = number_of_rooms
        self.__rating = rating
        self.__amenities = amenities
        self.__contact_number = contact_number

    # Getter and Setter methods for Hotel class
    def get_hotel_id(self):
        return self.__hotel_id

    def set_hotel_id(self, hotel_id):
        self.__hotel_id = hotel_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_number_of_rooms(self):
        return self.__number_of_rooms

    def set_number_of_rooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    def get_rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating = rating

    def get_amenities(self):
        return self.__amenities

    def set_amenities(self, amenities):
        self.__amenities = amenities

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    # Placeholder method to update room availability
    def update_room_availability(self):
        # This function will update the availability of rooms in the hotel
        pass


# Invoice Class: Manages invoices issued to guests after their stay
class Invoice:
    def __init__(self, invoice_id, reservation_id, guest_id, total_amount, date_issued, payment_status, room_number):
        # Private attributes for Invoice class
        self.__invoice_id = invoice_id
        self.__reservation_id = reservation_id
        self.__guest_id = guest_id
        self.__total_amount = total_amount
        self.__date_issued = date_issued
        self.__payment_status = payment_status
        self.__room_number = room_number

    # Getter and Setter methods for Invoice class
    def get_invoice_id(self):
        return self.__invoice_id

    def set_invoice_id(self, invoice_id):
        self.__invoice_id = invoice_id

    def get_reservation_id(self):
        return self.__reservation_id

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_guest_id(self):
        return self.__guest_id

    def set_guest_id(self, guest_id):
        self.__guest_id = guest_id

    def get_total_amount(self):
        return self.__total_amount

    def set_total_amount(self, total_amount):
        self.__total_amount = total_amount

    def get_date_issued(self):
        return self.__date_issued

    def set_date_issued(self, date_issued):
        self.__date_issued = date_issued

    def get_payment_status(self):
        return self.__payment_status

    def set_payment_status(self, payment_status):
        self.__payment_status = payment_status

    def get_room_number(self):
        return self.__room_number

    def set_room_number(self, room_number):
        self.__room_number = room_number

    # Placeholder method to generate invoice
    def generate_invoice(self):
        # This function will generate an invoice for the reservation
        pass


# ---------------------- Test Objects ----------------------

# Create a test Guest object based on the image
guest1 = Guest(101, "Ted H Vera", "tedvera@mac.com", "+505-661-1110", "2455 Trinity Drive, Los Alamos", "American", "1980-05-12")

# Create a test Room object based on the image
room1 = Room(202, "2 Queen Beds", 89.85, True, 2, 2, "No Smoking, Desk, Safe, Coffee Maker, Hair Dryer")

# Create a test Reservation object based on the image (with correct checkout date)
reservation1 = Reservation(563405086, "2024-08-22", "2024-08-24", 202, 101, "Confirmed", 2)

# Create a test Payment object based on the image
payment1 = Payment(801, 563405086, "Mastercard (ending in 1904)", 201.48, "2024-08-22", "Completed", "1904")

# Create a test Hotel Employee object (not directly shown in the image, so fictional data is used)
employee1 = HotelEmployee(301, "Alice Smith", "Receptionist", "Morning", "alice@hotel.com", "+987654321", "2020-01-15")

# Create a test Hotel object based on general assumptions
hotel1 = Hotel(401, "Comfort Inn & Suites Los Alamos", "2455 Trinity Drive, Los Alamos, NM", 1, 4.0, "Free Wi-Fi, Breakfast, Parking", "+505-661-1110")

# Create a test Invoice object based on the image
invoice1 = Invoice(52533887, 563405086, 101, 201.48, "2024-08-22", "Paid", 202)

# Print the complete reservation confirmation details similar to the image
print("Your Reservation Is Confirmed")
print("Thank you for your reservation. Please print your hotel receipt and show it at check-in.")
print(f"Your Name: {guest1.get_name()}")
print(f"Your Email: {guest1.get_email()}")
print(f"Priceline Trip Number: {reservation1.get_reservation_id()}")
print(f"Hotel Confirmation Number: {invoice1.get_invoice_id()}")
print()

# Print the hotel details section
print(f"{hotel1.get_name()}")
print(f"{hotel1.get_location()}")
print(f"Check-In Date: {reservation1.get_check_in_date()}, 03:00 PM")
print(f"Check-Out Date: {reservation1.get_check_out_date()}, 12:00 PM")
print(f"Number of Nights: {reservation1.get_num_of_nights()}")
print(f"Phone: {guest1.get_phone()}")
print(f"Room: {guest1.get_name()}")
print(f"Room Type: {room1.get_room_type()} - {room1.get_amenities()}")
print()

# Print the summary of charges
print("Summary of Charges")
print(f"Billing Name: {guest1.get_name()}")
print(f"Credit Card: {payment1.get_payment_method()}")
print(f"Room Cost: ${room1.get_price_per_night():.2f} per night")
print(f"Number of Rooms: 1")
print(f"Number of Nights: {reservation1.get_num_of_nights()}")
room_total = room1.get_price_per_night() * reservation1.get_num_of_nights()
print(f"Room Subtotal: ${room_total:.2f}")
taxes_fees = 21.58  # Taken from the image
print(f"Taxes and Fees: ${taxes_fees:.2f}")
total_charges = room_total + taxes_fees
print(f"Total Charges: ${total_charges:.2f}")



