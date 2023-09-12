# https://www.airnewzealand.co.nz/flights/en-nz/flights-from-auckland-to-wellington
# https://www.dthm4kaiako.ac.nz/resources/resource/74/csfg-ncea-guide-for-as91371-244/
import random
from time import sleep

#colouring
def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"
Error = rgb(255,105,105)
white = rgb(255,255,255)

#stuff
num_full_seat = 0
num_full_seat = random.randint(0, 248)

# num_people_ask catch
def num_people_ask():
	while True:
		try:
			num_people = int(input("how many people are coming with you(includeing you)? "))	
			if num_people > 0 and num_people < 249:
				print("it works")
				return num_people
				break
		except ValueError:
			print("exceeds the number of seats available or invald input")

# welcome user
print(f"{white}Hello user,")
name = input("What is your name? ")
print("Hello",name,"I hope you are having a good day. ")
npa = num_people_ask()
destination = int(input("""Where are you traveling to?
1 for Hamilton, 2 for Rotorua, 3 for Auckland. """))
fclass = int(input("""What class of flight would you like?
1 for first class, 2 for Business class, 3 for economy class. """))
leave_day = input("""when do are you planing on departing? 
'today', 'tomorrow', or the 'day after'. """)
leave_day = leave_day.strip().lower()
			
# destination stuff
if destination == 1:
	destination_price = 40
	destination = "Hamilton"
elif destination == 2:
	destination_price = 60
	destination = "Rotorua"
elif destination == 3:
	destination_price = 50
	destination = "Auckland"
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
num_full_seat += npa

# leaving logic
if leave_day == "today":
	leave_dayn = 1
elif leave_day == "tomorrow":
	leave_day_n = 2

#full price
full_price = 0
def work(full_price, destination_price, npa, class_price, num_full_seat):
	full_price += (destination_price * npa)
	full_price *= class_price
	if num_full_seat > 75:
		full_price *= 1.2
	return full_price
	print(full_price)
work(full_price, destination_price, npa, class_price, num_full_seat)

# user data
print("""name:""",name,"""
people""",npa,"""
destination:""",destination,"""
Seat Class:""",fclass,"""
full steats:""",num_full_seat,"""
Price:""",work(full_price, destination_price, npa, class_price, num_full_seat),"""
""")
