# Create an intro message for the user :) Come up with a good name
#names -> Map & Cheese
print("testing to see if this works on github")
print("\n-------------------Map & Cheese-----------------------")
print("Welcome to Map & Cheese! Been around since '21")
print("Visit our website -> www.mapandcheese.com")
print("Our business hours are at the bottom of our page :)")
print("------------------------------------------------------\n")


# We want to ask the user for their first & last name & age
first_name = input("Enter your first name:") # Hunter
last_name = input("Enter your last name: ") # Macias
print(f"Full Name: {first_name} {last_name}")
correct_name = input("Is your name entered correctly? ") # yes
if correct_name != 'yes':
	first_name = input("Enter your first name:") # Matthew
	last_name = input("Enter your last name: ") # Macias
	print(f"Updated Full Name: {first_name} {last_name}")


age = int(input("Enter your age: ")) # 20
print(f"Age: {age}")
correct_age = input("Did you enter your age correctly? ") #no
if correct_age != "yes":
	age = int(input("Enter your age: ")) # 20
	print(f"Updated Age: {age}")



# We want to ask the user for their phone number
phone_number = input("Enter your phone number: ")
print(f"You entered {phone_number} for your number")
correct_number = input("Did you enter your phone number correctly? ") #no
if correct_number != "yes":
	phone_number = int(input("Enter your phone number again: ")) # 20
	print(f"Updated phone number: {phone_number}")
# We want to ask the user if they want takeout or delivery 

# We want to ask what cuisine they want

# We want to ask the user for their current address

# Calculating Distances...


