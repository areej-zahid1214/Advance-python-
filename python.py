menu={
   "pizza":3000,
   "cold-drink":200,
   "shuarma":650,
   "burger":650,
   "pasta":1500,
}
print(menu)
total_bill=0
n = int(input("how much order did you want? "))

for i in range(1, n + 1):
    order = input(f"Enter item {i}: ")
if order in menu:
    total_bill += menu[order]
else:
    print("Sorry, yeh item menu mein nahi hai!")

if (total_bill>=1500):
  total_bill=total_bill-(total_bill*0.10)
  print("your bill with discount is ",total_bill)
elif ( total_bill==0):
    print(" Sorry!....There is no things in the order")
else:
    print("your bill is",total_bill)