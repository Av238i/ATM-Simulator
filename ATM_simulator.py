print("ATM SIMULATOR".center(75))
print()
correct_pin=1234
balance=10000
attempts_made=0
access=False
program_running=True
while attempts_made<3 and access==False:
    pin=int(input("Enter your 4-digit PIN:"))
    if pin==correct_pin:
        access=True
    else:
        attempts_made=attempts_made+1
        attempts_left=3-attempts_made
        print("Incorrect PIN")
        print("Attempts left:",attempts_left)
        if attempts_left==1:
            print("HINT: The demo PIN is 1234")
            print()
if access==True:
    while program_running:
        print()
        print("1.Check Balance")
        print("2.Deposit amount in account")
        print("3.Withdraw money from account")
        print("4.exit")
        choice=input("Enter Choice:")
        print()
        if choice=='1':
            print("Your balance is: Rs.", balance)
        elif choice=='2':
            amount=float(input("Enter amount to deposit: Rs."))
            if amount<=0:
                print("Invalid Amount")
            else:
                balance=balance+amount
                print("Deposited to account. New balance: Rs.", balance)
        elif choice=='3':
            amount=float(input("Enter amount to withdraw: Rs."))
            if amount<=0:
                print("Invalid Amount")
            elif amount>balance:
                print("Insufficient Balance")
            else:
                balance=balance-amount
                print("Withdrawn from account. New balance: Rs",balance)
        elif choice=='4':
            print("Thank you For using the ATM. Goodbye!")
            program_running=False
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            print()
else:
    print("Too many incorrect attempts. Card Declined.")
            
                
