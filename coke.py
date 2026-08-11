# The program simulates a vending machine that sells a coke for 50 cents. It accepts coins of 5, 10, and 25 cents. The user is prompted to insert coins until the total amount inserted is equal to or greater than the price of the coke. If the user inserts an invalid coin or input, they are prompted to try again. Once the total amount is sufficient, the program calculates and displays the change to be returned.
# Ask for coin as integer
def main():
    price = 50
    total = 0
    
    # Get user input for coin
    while total < price:
        try: 
            coin = int(input("Insert coin (in cents): "))
            if coin in [5, 10, 25]:
                total += coin
                print(f"Total inserted: {total} cents, Amount due {price - total} cents")
            else: 
                print("Invalid coin. Please insert a valid coin (5, 10, 25 cents).")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Calculate change and print result
    change = total - price
    print(f"Here is your coke and your change is: {change} cents")

# Call the main function
main()
   

