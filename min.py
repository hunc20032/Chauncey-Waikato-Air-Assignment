			destination = int(input("""Where are you traveling to?
1 for Hamilton($39.99), 2 for Rotorua($59.99), 3 for Auckland($54.99). """))	
			if destination == 1:
				destination_price = 39.99
				destination = "Hamilton"
				return destination_price,destination
				break
			elif destination == 2:
				destination_price = 59.99
				destination = "Rotorua"
				return destination_price,destination
				break
			elif destination == 3:
				destination_price = 54.99
				destination = "Auckland"
				return destination_price,destination
				break
			else:
				print("invald input")
		except ValueError:
			print("invald input")

# flight class catch
def seat():
	while True:
	def seat():
				break
			elif fclass == 2:
				fclass = "Business class"
				class_price = 1.6
				return class_price,fclass
				break
			elif fclass == 3:
				fclass = "economy class"
				class_price = 1.1
				return class_price,fclass
				break
			else:
				print("invald input")
		except ValueError:
			print("invald input")

# when leave 
def leafd():
	while True:
		try:
			leave_day = int(input("""when do are you planing on departing? 
1 for today, 2 for tomorrow, 3 for the day after, or 4 for other. """))
			if leave_day == 1:
				leave_day = "First class"
				leave_price = 1.8
				return leave_price,leave_day
				break
			elif leave_day == 2:
				leave_day = "Business class"
				leave_price = 1.6
				return leave_price,leave_day
				break
			elif leave_day == 3:
				leave_day = "economy class"
				leave_price = 1.4
				return leave_price,leave_day
				break
			elif leave_day == 4:
				leave_day = "economy class"
				leave_price = 1.1
				return leave_price,leave_day
				break
			else:
				print("invald input")
		except ValueError:
			print("invald input")

# talk to user
print(f"{white}Hello and welcome to Waikato airborn,")
name = input("What is your name? ")
print("Hello",name,"I hope you are having a good day. ")
num_people_ask = npa()
destination_price = des()
fclass = seat()
leave_day = leafd()

# seats left
num_full_seat += num_people_ask

#full price
full_price = 0
def work(full_price, destination_price, num_people_ask, fclass, num_full_seat):
	full_price += (destination_price[0] * num_people_ask)
	full_price *= fclass[0]
	if num_full_seat > 75:
		full_price *= 1.2
	full_price *=leave_day
	full_price = round(full_price, 2)
	return full_price
work(full_price, destination_price, num_people_ask, fclass, num_full_seat)

# user data
def work(full_price, destination_price, num_people_ask, fclass, num_full_seat):
full steats:""",num_full_seat,"""
Price:""",work(full_price, destination_price, num_people_ask, fclass, num_full_seat),"""
""")
confirm = input("Confirm? Y or N ")