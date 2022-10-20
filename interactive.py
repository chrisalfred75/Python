print("Welcome to Pagoto Wagon!! May I know your name?")
name = input()
print("Hello " + name + "!! What is your age ??" )
age = input()
print("Just "+ age + "!! You are younger than me. LOL !!")
print("Please enter your phone number to be a regualar customer of Icecream Wagon who benefits all our offers!!")
number = input()
print("Just verify your number " + number + " If not, please enter 1. If yes, Please enter 2.")
confirm = input()
if confirm == 2:
    print("Thanks for your confirmation. Your Registration with Pagoto Wagon is completed.")
else:
    print("Please enter your mobile number once again.")
    rnumber = input()
    print("Your mobile number is "+ rnumber + ". Thank you for registering with Icecream Wagon.")

