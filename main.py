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
destination = int(input("""Where are you going to?
1 for Hamilton, 2 for Rotorua, 3 for Auckland. """))
clawss = int(input("""What class of flight would you like?
"""))
# destination stuff
if destination == 1:
	destination_price = 1
	destination = "Ham"
elif destination == 2:
	destination = "Rat"
elif destination == 3:
	destination = "Duckland"
else:
	print("you suck")
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
