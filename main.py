# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
  bill = 15
elif size == "M":
  bill = 20
elif size == "L":
  bill = 25
else:
 print("enter a valid size")


if add_pepperoni == "Y":
  bill += 2

if extra_cheese == "Y":
  bill += 1


print(f"your final bill is ${bill}")

# if size == "s":
#   bill = 15
# elif size == "m":
#   bill = 20
# elif size == "l":
#   bill = 25
# else:
#   print("enter a valid size")

# if add_pepperoni == "Y":
#   if size == "s":
#     bill += 2
#   else:
#     bill += 3
# else:
#   bill = bill


# if extra_cheese == "Y":
#   bill += 1
# else:
#   bill = bill
  
# print(f"your final bill is ${bill}")