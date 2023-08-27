# https://www.airnewzealand.co.nz/flights/en-nz/flights-from-auckland-to-wellington
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
1 for first class, 2 for busniss class, 3 for economy class."""))

# destination stuff
if depart == 1 and destination == 2:
	destination_price = 100
	depart = "Rat"
	destination = "ham"
elif depart == 1 and destination == 2:
	destination_price = 150
	depart = "Ham"
	destination = "rat"
elif destination == 3:
	destination = "duckland"
else:
	print("you suck")

#flight class stuff
if fclass == 1:
	fclass
# grouping age groups
older = num_old + num_adult
younger = num_teen + num_bigbaby + num_baby

#full price
full_price = 0
full_price += (num_old * 40)
full_price += (num_adult * 100)
full_price += (num_teen * 80)
full_price += (num_bigbaby * 60)
full_price += (num_baby * 40)

# user data
print("""name:""",name,"""
Adults:""",num_adult,"""
Teens:""",num_teen,"""
children:""",num_bigbaby,"""
baby:""",num_baby,"""
destination:""",destination,"""

price:""",full_price,"""
""")
