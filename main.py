# import libraries
import random
import sys


# classmethodheck if there are numbers in a values
def contains_number(string):
	return any(char.isdigit() for char in string)
	
# ask where they would like to travel to and tell them the price of the flight
# return the place and price to be used later
def get_destination_price():
	while True:
		try:
			destination = int(input("""Where are you traveling to?
1 for Hamilton($39.99), 2 for Rotorua($59.99), 3 for Auckland($54.99). """))    
			if destination == 1:
				return 39.99, "Hamilton"
			elif destination == 2:
				return 59.99, "Rotorua"
			elif destination == 3:
				return 54.99, "Auckland"
			else:
				print("Invalid input")
		except ValueError:
			print("Invalid input")

# ask how many people they are booking for and tell them how many seats are left
# return the number of people to be used later and change the total number of people on the flight
def get_num_people(destination_price):
	while True:
		try:
			if destination_price[0] == 54.99:
				print("We have",248 - full_bookings["Auckland"],"seats left on the Auckland flight ")
				num_people = int(input("How many people are you booking for? "))
				if 0 < num_people and num_people < (249 - full_bookings["Auckland"]):
					full_bookings["Auckland"] += num_people
					return full_bookings["Auckland"], num_people
				else:
					print("Exceeds the number of seats available")
					
			elif destination_price[0] == 39.99:
				print("We have",248 - full_bookings["Hamilton"],"seats left on the Hamilton flight ")
				num_people = int(input("How many people are you booking for? "))
				if 0 < num_people and num_people < (249 - full_bookings["Hamilton"]):
					full_bookings["Hamilton"] += num_people
					return full_bookings["Hamilton"], num_people
				else:
					print("Exceeds the number of seats available")
					
			elif destination_price[0] == 59.99:
				print("We have",248 - full_bookings["Rotorua"],"seats left on the Rotorua flight ")
				num_people = int(input("How many people are you booking for? "))
				if 0 < num_people and num_people < (249 - full_bookings["Rotorua"]):
					full_bookings["Rotorua"] += num_people
					return full_bookings["Rotorua"], num_people
				else:
					print("Exceeds the number of seats available")

		except ValueError:
			print("Invalid input")

# ask user what class of seat they want and tell them the price of the seat
# return the seat class and price to be used later
def get_seat_class():
	while True:
		try:
			fclass = int(input("""What class of flight would you like?
1 for first class(2x$), 2 for Business class(1.6x$), 3 for economy class(1.1x$). """))
			if fclass == 1:
				return 2, "First class"
			elif fclass == 2:
				return 1.6, "Business class"
			elif fclass == 3:
				return 1.1, "economy class"
			else:
				print("Invalid input")
		except ValueError:
			print("Invalid input")

# ask user when they want to depart
# return the day and price to be used later
def get_leave_day():
	while True:
		try:
			leave_day = int(input("""When are you planning on departing?
1 for tomorrow, 2 for the day after, or 3 for a later date. """))
			if leave_day == 1:
				return 1.8, "tomorrow"
			elif leave_day == 2:
				return 1.5, "after tomorrow"
			elif leave_day == 3:
				return 1.1, "other day"
			else:
				print("Invalid input")
		except ValueError:
			print("Invalid input")

# ask user there name and check if it is suitable
def get_username():
	while True:
		try:
			name = input("What is your username? ")
			namelength = len(name)
			if namelength >= 2 and contains_number(name) == False:
				break
			elif contains_number(name) == True:
				print("username may not contain numbers")
			elif namelength < 2:
				print("username must be at least 2 characters")
			else:
				print("Invalid input")
		except ValueError:
			print("Invalid input")
	print(f"Hello {name}, I hope you are having a good day. ")
	return name

# calculate the total price
def calculate_full_price(destination_price, num_people_ask, fclass, leave_day):
	full_price = (destination_price[0] * num_people_ask[1]) * fclass[0]
	if num_people_ask[0] > 124:
		full_price *= 1.2
	full_price *= leave_day[0]
	full_price = round(full_price, 2)
	return full_price

# Print the ticket information
def print_ticket_info(name, num_people_ask, destination_price, fclass, leave_day, full_price):
	print(f"""
	Username: {name}
	Full seats: {num_people_ask[0]}
	People coming: {num_people_ask[1]}
	Destination: {destination_price[1]}
	Seat Class: {fclass[1]}
	Flight Date: {leave_day[1]}
	Price: ${full_price}""")
	num_tickets = num_people_ask[0]
	for i in range(num_people_ask[1]):
		num_tickets += 1
		print(f"	Ticket number: {num_tickets}")

# Ask the user if they want to book another ticket and repeat the questions
def ask_second_booking():
	while True:
		try:
			booking_confirmation = input("Would you like to book another ticket? (Y/N)" )
			booking_confirmation = booking_confirmation.upper().strip()
			if booking_confirmation == "Y":
				print("Hello and welcome to Waikato airborn,")
				name = get_username()
				destination_price = get_destination_price()
				num_people_ask = get_num_people(destination_price)
				fclass = get_seat_class()
				leave_day = get_leave_day()
				full_price = calculate_full_price(destination_price, num_people_ask, fclass, leave_day)
				print_ticket_info(name, num_people_ask, destination_price, fclass, leave_day, full_price)
				middle_man()
			elif booking_confirmation == "N":
				sys.exit()
			else:
				print("Invalid input")
		except ValueError:
			print("Invalid input")

# making repeating ask unless the used declines
def middle_man():
	ask_second_booking()

# Generate random bookings (fix me)
full_bookings = {
	"Auckland": random.randint(0, 247),
	"Hamilton": random.randint(0, 247),
	"Rotorua": random.randint(0, 247)}

# run all defs
print("Hello and welcome to Waikato airborn,")
name = get_username()
destination_price = get_destination_price()
num_people_ask = get_num_people(destination_price)
fclass = get_seat_class()
leave_day = get_leave_day()
full_price = calculate_full_price(destination_price, num_people_ask, fclass, leave_day)
print_ticket_info(name, num_people_ask, destination_price, fclass, leave_day, full_price)

ask_second_booking()
