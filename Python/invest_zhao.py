# Name: Kevin Zhao
# Date: 11/22/23
# Program: invest_zhao.py
# Compute and display an investment report for compound interest

def main():
    # Gather inputs
    startBalance = float(input("Enter the investment amount: "))    # float
    years = int(input("Enter the number of years: "))               # int
    rate = int(input("Enter the interest rate as a %: "))           # int

    # Convert the percent rate to a decimal
    rate = rate / 100

    # Initialize interest accumulator
    totalInterest = 0.0

    # Display the header for the table 
    print("{0:>4}{1:>18}{2:>10}{3:>16}".format("Year", "Starting Balance", "Interest", "Ending Balance"))

    # Compute and display the results for each year
    for year in range(1, years+1):
        interest = startBalance * rate          # Calculate interest
        endBalance = startBalance + interest    # Calculate endBalance

        # print formatted results for each year
        print("{0:>4}{1:>18.2f}{2:>10.2f}{3:>16.2f}".format(year, startBalance, interest, endBalance))

        startBalance = endBalance               # Update startBalance for the next year
        totalInterest += interest               # Update totalInterest

    # Display Ending Balance
    print("Ending Balance: $" + str(round(endBalance, 2)))

    # Display Total Interest Earned
    print("Total Interest earned: $" + str(round(totalInterest, 2)))

main()
    
