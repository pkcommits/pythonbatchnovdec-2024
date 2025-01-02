"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""

P = float(input("Enter the principal amount (P): "))
R = float(input("Enter the rate of interest (R): "))
T = float(input("Enter the time in years (T): "))

# Simple Interest calculation using the formula SI = (P * R * T) / 100
SI = (P * R * T) / 100
print(f"Simple Interest (SI): {SI}")

# Monthly repayment with Simple Interest
total_amount_si = P + SI
monthly_payment_si = total_amount_si / (T * 12)
print(f"Monthly repayment with Simple Interest: {monthly_payment_si:.2f}")

# Compound Interest calculation using the formula100 CI = P * ((1 + R / 100) ** T) - P
CI = P * ((1 + R / 100) ** T) - P
print(f"Compound Interest (CI): {CI}")

# Monthly repayment with Compound Interest
total_amount_ci = P + CI
monthly_payment_ci = total_amount_ci / (T * 12)
print(f"Monthly repayment with Compound Interest: {monthly_payment_ci:.2f}")10











# Assignment
# 1. Compound Interest Calculation
#     ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php
