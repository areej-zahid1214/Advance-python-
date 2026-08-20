User=(input("Enter your name"  ))
age=int(input("Enter your age"  ))
day=(input("Whats the day" )).strip().lower()
promo_code="Discount20"
ticket_Quantity=int(input("Enter the Quantity of Tickets what you Want"  ))
base_price=800.0
total_Price=ticket_Quantity*base_price
if (age<=12 or age>=60):
    final_price=total_Price-(total_Price/2)
    print("50% Discount is",final_price)
elif (User==promo_code):
    final_price=total_Price-(total_Price*0.3)
    print('60% Discount is',final_price) 
elif (day=="saturday" or day=="sunday"):
    final_price=total_Price+(100*ticket_Quantity)
    print("charges of Ticket is Extra Due to week days" ,final_price)
else:
    print("Your Ticket price is",total_Price)
    
     