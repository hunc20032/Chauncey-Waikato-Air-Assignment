# https://www.airnewzealand.co.nz/flights/en-nz/flights-from-auckland-to-wellington
# https://www.dthm4kaiako.ac.nz/resources/resource/74/csfg-ncea-guide-for-as91371-244/
import random

#stuff
num_people = 1
num_full_seat = 0
num_full_seat = random.randint(0, 100)

# welcome user
print("Hello user,")
name = input("What is your name? ")
print("Hello",name,"I hope you are having a good day. ")
num_people = int(input("how many people are coming with you(includeing you)? "))
depart = int(input("""Where are you taking off from?
1 for Hamilton, 2 for Rotorua, 3 for Auckland. """))
destination = int(input("""Where are you traveling to?
1 for Hamilton, 2 for Rotorua, 3 for Auckland. """))
fclass = int(input("""What class of flight would you like?
1 for first class, 2 for Business class, 3 for economy class. """))
leave_day = input("""when do are you planing on departing? 
'today', 'tomorrow', or the 'day after'. """)
leave_day = leave_day.strip().lower()

# destination stuff
if depart == 1 and destination == 2:
	destination_price = 50
	depart = "Hamilton"
	destination = "Rotorua"
elif depart == 1 and destination == 3:
	destination_price = 70
	depart = "Hamilton"
	destination = "Auckland"
elif depart == 2 and destination == 1:
	destination_price = 60
	depart = "Rotorua"
	destination = "Hamilton"
elif depart == 2 and destination == 3:
	destination_price = 130
	depart = "Rotorua"
	destination = "Auckland"
elif depart == 3 and destination == 1:
	destination_price = 80
	depart = "Auckland"
	destination = "Hamilton"
elif depart == 3 and destination == 2:
	destination_price = 140
	depart = "Auckland"
	destination = "Rotorua"
else:
	print("you suck")

# flight class stuff
if fclass == 1:
	fclass = "First class"
	class_price = 3
elif fclass == 2:
	fclass = "Business class"
	class_price = 2
elif fclass == 3:
	fclass = "economy class"
	class_price = 1
# seats left
num_full_seat += num_people

#full price
full_price = 0
def work(full_price, destination_price, num_people, class_price, num_full_seat):
	full_price += (destination_price * num_people)
	full_price *= class_price
	if num_full_seat > 75:
		full_price *= 1.2
	return full_price
	print(full_price)
work(full_price, destination_price, num_people, class_price, num_full_seat)

# user data
print("""name:""",name,"""
people""",num_people,"""
destination:""",destination,"""
Seat Class:""",fclass,"""
full steats:""",num_full_seat,"""
Price:""",work(full_price, destination_price, num_people, class_price, num_full_seat),"""
""")
