# https://www.airnewzealand.co.nz/flights/en-nz/flights-from-auckland-to-wellington
# https://www.dthm4kaiako.ac.nz/resources/resource/74/csfg-ncea-guide-for-as91371-244/
import random
#stuff
num_old = 1
num_adult = 1
num_teen = 1
num_bigbaby = 1
num_baby = 1
num_full_seat = 0
num_full_seat = random.randint(0, 100)
# welcome user
print("Hello user,")
name = input("What is your name? ")
print("Hello",name,"I hope you are having a good day. ")
num_old = int(input("How many ealdery do you have(age 70+) are you booking for? "))
num_adult = int(input("How many adults(age 19+) are you booking for? "))
num_teen = int(input("How many teens(age 13+) are you coming with you? "))
num_bigbaby = int(input("How many children(age 2+) are you coming with you? "))
num_baby = int(input("How many baby are you coming with you? "))
depart = int(input("""Where are you taking off from?
1 for Hamilton, 2 for Rotorua, 3 for Auckland. """))
destination = int(input("""Where are you traveling to?
1 for Hamilton, 2 for Rotorua, 3 for Auckland. """))
fclass = int(input("""What class of flight would you like?
1 for first class, 2 for Business class, 3 for economy class. """))

# destination stuff
if depart == 1 and destination == 2:
	destination_price = 50
	depart = "Ham"
	destination = "Rat"
elif depart == 1 and destination == 3:
	destination_price = 70
	depart = "Ham"
	destination = "Duck"
elif depart == 2 and destination == 1:
	destination_price = 60
	depart = "Rat"
	destination = "Ham"
elif depart == 2 and destination == 3:
	destination_price = 130
	depart = "Rat"
	destination = "Duck"
elif depart == 3 and destination == 1:
	destination_price = 80
	depart = "Duck"
	destination = "Ham"
elif depart == 3 and destination == 2:
	destination_price = 140
	depart = "Duck"
	destination = "Rat"
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
num_full_seat += num_old + num_adult + num_teen + num_bigbaby

#full price
def price():
	full_price = 0
	full_price += (destination_price * num_old * 0.5)
	full_price += (destination_price * num_adult)
	full_price += (destination_price * num_teen * 0.8)
	full_price += (destination_price * num_bigbaby * 0.65)
	full_price += (destination_price * num_baby * 0.5)
	full_price *= class_price
	if num_full_seat > 75:
		full_price *= 1.2
	return full_price
price()
# user data
print("""name:""",name,"""
Elderly:""",num_old,"""
Adults:""",num_adult,"""
Teens:""",num_teen,"""
children:""",num_bigbaby,"""
baby:""",num_baby,"""
destination:""",destination,"""
Seat Class:""",fclass,"""
full steats:""",num_full_seat,"""
Price:""",full_price,"""
""")
