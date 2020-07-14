# Create a function that will take all your coins and convert it to the cash amount.

    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.

def calc_dollars(**coins):

    cash_total = 0
    
    for key, value in coins.items():
        if key == "pennies":
            cash_total += value*.01

        if key == "nickels":
            cash_total += value*.05    

        if key == "dimes":
            cash_total += value*.10
        
        if key == "quarters":
            cash_total += value*.25
            
    print(cash_total)
    

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)