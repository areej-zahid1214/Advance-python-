# CLI-based calculator 

# a=int(input("Enter The 1st no "))
# b=int(input("Enter The 2nd  no"))
# choice=input("Enter your choice")
# if choice =="+" :
#     print("Sum of two no is :" ,a+b)
# elif choice =="-" :
#     print("Sub of two no is :" ,a-b)
# elif choice =="*" :
#     print("MUl of two no is :" ,a*b)
# elif choice =="**" :
#     print(" Power Multi of two no is :" ,a**b)
# elif choice =="/" :
#     print("divi of two no is :" ,a/b)
# elif choice =="%" :
#     print("Remain of two no is :" ,a%b)
# else:
#     print("plz enter the Valid Choice")   



#   Guessing Game

# num=int(input("Enter The no "))
# choose=("Choose the no between 900")
# if num==8:
#     print("Congratulation:","you win")
# elif num==899:
#     print("hy keep it up bacchy:","you  Can do it")
# elif  num==800:
#     print("You Did it:","try Again")    
# else:
#     print("sorry","you lose it")   

    
# #  Smart Movie Ticket Pricing System  
# base_price = 800
# age = int(input("Enter the age: "))
# choose_the_standard = input("Select the format (Standard, 3D, IMAX): ")
# if age < 12:
#     ticket_price = base_price / 2
#     print("Category: Child (Half Price)")

# elif age >= 12 and age <= 60:
#     ticket_price = base_price
#     print("Category: Adult (Full Price)")

# else:
#     ticket_price = base_price * 0.75
#     print("Category: Senior Citizen (25% Discount)")

# if choose_the_standard == "3D":
#     ticket_price = ticket_price + 300
#     print("Extra charges added for 3D (+300)")

# elif choose_the_standard == "IMAX":
#     ticket_price = ticket_price + 500
#     print("Extra charges added for IMAX (+500)")

# elif choose_the_standard == "Standard":
#     print("Standard format selected (No extra charges)")

# else:
#     print("Invalid format entered, charging base ticket price.")
# print("Your Total Final Bill is:", ticket_price)
    
    
    
#  ATM PIN Security Simulator
# pin = 123
# i = 0
# max_attempt = 3

# while i < max_attempt:
#     password = int(input("Enter the pin: "))
#     if password == pin:
#         print("Access Granted! Welcome.")
#         break
#     else:
#         i += 1  
#         remaining_attempts = max_attempt - i
#         if remaining_attempts > 0:
#             print("Wrong PIN! You have {remaining_attempts}  left.")
#         else:
#             print("Your card is blocked.")

      
 
# #  Custom Multiplication Table Generator    
    
# num1=int(input("Enter the no ")) 
# end_limit=int(input("Enter the no ")) 
# for i in range(1,end_limit+1):
#     result=num1*i
#     print(f"{num1} * {i} = {result}")

 


        
