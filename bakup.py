# import libraries
import random


def get_destination_price():
	while True:
		try:
			# Prompt the user for the destination they are traveling to
			destination = int(input("""Where are you traveling to?
1 for Hamilton($39.99), 2 for Rotorua($59.99), 3 for Auckland($54.99). """))    
			if destination == 1:
				# Return the price and name of the destination selected
				return 39.99, "Hamilton"
			elif destination == 2:
				return 59.99, "Rotorua"
			elif destination == 3:
				return 54.99, "Auckland"
			else:
				print("Invalid input")
		except ValueError:
			print("Invalid input")

def get_num_people():
	while True:
		try:
			num_full_seat = 0
			if destination_price[0] == 54.99:
				num_full_seat = full_bookings["Auckland"]
				print(f"We have {248 - num_full_seat} seats left on the Auckland flight ")
			elif destination_price[0] == 39.99:
				num_full_seat = full_bookings["Hamilton"]
				print(f"We have {248 - num_full_seat} seats left on the Hamilton flight ")
			elif destination_price[0] == 59.99:
				num_full_seat = full_bookings["Rotorua"]
				print(f"We have {248 - num_full_seat} seats left on the Rotorua flight ")

			# Prompt the user for the number of people booking
			num_people = int(input("How many people are you booking for? "))
			if 0 < num_people < (249 - num_full_seat):
				return num_full_seat + num_people, num_people
			else:
				print("Exceeds the number of seats available")
		except ValueError:
			print("Invalid input")

def get_seat_class():
	while True:
		try:
			# Prompt the user for the class of the flight
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

def get_leave_day():
	while True:
		try:
			# Prompt the user for the departure day
			leave_day = int(input("""When are you planning on departing?
Type... 1: tomorrow, 2: the day after, or 3: a later date. """))
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

def calculate_full_price(destination_price, num_people_ask, fclass, leave_day):
	# Calculate the full price based on the input values
	full_price = (destination_price[0] * num_people_ask[1]) * fclass[0]
	if num_people_ask[0] > 124:
		full_price *= 1.2
	full_price *= leave_day[0]
	full_price = round(full_price, 2)
	return full_price

def print_ticket_info(name, num_people_ask, destination_price, fclass, leave_day, full_price):
	# Print the ticket information
	print(f"""
	Username: {name}
	Full seats: {num_people_ask[0]}
	People coming: {num_people_ask[1]}
	Destination: {destination_price[1]}
	Seat Class: {fclass[1]}
	Flight Date: {leave_day[1]}
	Price: ${full_price}
	Ticket number: {random.randint(1, 248)}
	""")

# Generate random bookings
full_bookings = {
	"Auckland": random.randint(0, 248),
	"Hamilton": random.randint(0, 248),
	"Rotorua": random.randint(0, 248)
}

print("Hello and welcome to Waikato airborn,")
name = input("What is your username? ")
print(f"Hello {name}, I hope you are having a good day. ")

destination_price = get_destination_price()
num_people_ask = get_num_people()
fclass = get_seat_class()
leave_day = get_leave_day()

full_price = calculate_full_price(destination_price, num_people_ask, fclass, leave_day)
print_ticket_info(name, num_people_ask, destination_price, fclass, leave_day, full_price)
again = input("Would you like to book another ticket? (y/n) ")
if again == "y":

else:
	print("Thank you for using Waikato airborn, have a nice day!")