import math

# This program allows the user to access two different financial calculators: an investment and a home loan repayment calculator.
# It will calculate and retun the appropriate results to the user based on their calculator choice and input. 

# Menu for the user to choose the calculator with safeguarding for the correct input.
print('investment - to calculate the amount of interest you\'ll earn on your investment\n\
bond       - to calculate the amount you\'ll have to pay on a home loan\n')

customer_calc_choice = input('Enter either \'investment\' or \'bond\' from the menu above to proceed: ').lower()

while True:
    if customer_calc_choice not in ('bond', 'investment'):
        customer_calc_choice = input('\nInvalid entry. Please try again and enter either \'bond\' or \'investment\' to proceed: ').lower()
    else:
        print(f'\nThank you for selecting \'{customer_calc_choice}\'.\n')
        break

# Investment calculator.
# Ask for input about amount of money deposited, interest rate number, number of years for investment, choose between simple and compound interest.
# Finally, calculate the final investment figure based on customer choices and print it.
while customer_calc_choice == 'investment':
    deposit_amount = int(input('Please enter the amount of money you are depositing: '))
    interest_rate = int(input('Please enter the interest rate as number: '))
    years_investment = int(input('Please enter the number of years you plan on investing: '))
    interest = input('Please choose the correct interest type by entering either \'simple\' or \'compound\': ')
    
    if interest == 'simple':
        total_investment = deposit_amount * (1 + (interest_rate/100) * years_investment)
    else:
        total_investment = deposit_amount * (1 + (interest_rate/100))**years_investment

    print(f'\nThe result for your investment with interest type \'{interest}\' is {round(total_investment,2)}.')    
    
    break

# Bond calculator.
# Ask for input about present house value, interest rate number, number of months planned to take to repay the bond.
# Finally, calculate the monthly repayment figure and print it.
while customer_calc_choice == 'bond':
    house_value = int(input('Please enter the present value of your house: '))
    interest_bond = int(input('Please enter the interest rate as number: '))
    repay_time = int(input('Please enter the number of months you plan to take to repay the bond: '))

    total_investment = ((interest_bond/100/12) * house_value)/(1 - (1 + (interest_bond/100/12))**(-repay_time))
    
    print(f'\nThe amount of money you will have to repay each month is {round(total_investment,2)}')

    break


    