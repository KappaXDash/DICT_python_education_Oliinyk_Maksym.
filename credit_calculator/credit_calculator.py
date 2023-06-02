import argparse
import math

# create an argument parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument('--type')
parser.add_argument('--principal', type=float)
parser.add_argument('--interest', type=float)
parser.add_argument('--annuity', type=float)
parser.add_argument('--payment', type=float)
parser.add_argument('--periods', type=int)

# parse the arguments
args = parser.parse_args()

# assign the arguments to variables
loan_type = args.type
principal = args.principal
interest = args.interest
annuity = args.annuity
payment = args.payment
periods = args.periods

# check if the loan type is provided
if loan_type is None:
    print("Loan type is not specified. Please provide --type argument.")
    exit(1)

# check the type of the loan and calculate accordingly
if loan_type == "annuity":
    if not annuity:
        if not all([principal, interest, periods]):
            print("Incomplete parameters. Please provide --principal, --interest, and --periods.")
            exit(1)
        interest_rate = interest / (12 * 100)
        annuity = math.ceil(principal * (interest_rate * pow((1 + interest_rate), periods)) / (pow((1 + interest_rate), periods) - 1))
        overpayment = annuity * periods - principal
        print(f'Your monthly payment = {annuity}!\nOverpayment = {overpayment}')
    else:
        print("Invalid combination of parameters. Please provide either --annuity or other relevant parameters.")
        exit(1)
elif loan_type == "diff":
    if not all([principal, interest, periods]):
        print("Incomplete parameters. Please provide --principal, --interest, and --periods.")
        exit(1)
    interest_rate = interest / (12 * 100)
    total_payment = 0
    for month in range(1, periods + 1):
        differential_payment = math.ceil(principal / periods + interest_rate * (principal - (principal * (month - 1)) / periods))
        total_payment += differential_payment
        print(f"Month {month}: payment is {differential_payment}")
    overpayment = total_payment - principal
    print(f'\nOverpayment = {overpayment}')
else:
    print("Invalid loan type. Please provide a valid --type argument.")
    exit(1)
