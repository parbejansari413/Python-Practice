Age = int(input("Enter your age; "))
if(Age >= 60):
    print("Senior Citizen Ticket: ")
elif(Age > 13):
    print("Regular Ticket: ")
elif(Age > 5):
    print("Child Ticket: ")
else:
    print("Free Ticket: ")


