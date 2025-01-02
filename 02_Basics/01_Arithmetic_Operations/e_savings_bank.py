"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

balance = 0

# Step 2: Initial Deposit of minimum balance
initial_deposit = 1500
balance += initial_deposit
print(f"Initial deposit of 1500 made. Current Balance: {balance:.2f}")

# Step 3: Salary credited
salary = 3300
balance += salary
print(f"Salary of 3300 credited. Current Balance: ${balance:.2f}")

# Step 4: Online Purchase
online_purchase = 33.33
balance -= online_purchase
print(f"Online purchase of 33.33 deducted. Current Balance: ${balance:.2f}")

# Step 5: House Rent Payment
house_rent = 1500
balance -= house_rent
print(f"House rent of 1500 paid. Current Balance: ${balance:.2f}")

# Step 6: Display Final Balance
print(f"\nFinal Balance: ${balance:.2f}")