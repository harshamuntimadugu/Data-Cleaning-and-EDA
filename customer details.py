print("==============CREATE CUSTOMER DETAILS====================")

customer = {
    "Customer ID": "CUST101",
    "Customer Name": "Harsha",
    "Age": 21,
    "Account Type": "Savings",
    "Branch": "Chennai",
    "Balance": 40000
}

print(customer)



print("========ADD NEW INFORMATION======================")

customer["Phone Number"] = "9876543210"
customer["Email"] = "harsha@gmail.com"



print("\n===== UPDATED CUSTOMER INFORMATION =====")
print(customer)



print("\n===== CUSTOMER ACCOUNT DETAILS =====")

print("Customer Name:", customer.get("Customer Name"))
print("Account Type:", customer.get("Account Type"))
print("Branch:", customer.get("Branch"))
print("Account Balance:", customer.get("Balance"))



customer["Phone Number"] = "9123456780"
customer["Branch"] = "andhra"

print("\n===== UPDATED INFORMATION =====")

print("New Phone Number:", customer.get("Phone Number"))
print("New Branch:", customer.get("Branch"))


print("=================DEPOIST MONEY==================")

previous_balance = customer.get("Balance")
deposit = 5000

updated_balance = previous_balance + deposit

customer["Balance"] = updated_balance


print("Previous Balance:", previous_balance)
print("Deposit:", deposit)
print("Updated Balance:", customer.get("Balance"))


print("=========WITHDRAWAL MONEY===============")

withdrawal = 3000

current_balance = customer.get("Balance")
updated_balance = current_balance - withdrawal

customer["Balance"] = updated_balance


print("Withdrawal:", withdrawal)
print("Updated Balance:", customer.get("Balance"))


# STEP 7 — FINAL ACCOUNT REPORT

print("================================")
print("      FINAL ACCOUNT REPORT")
print("================================")

print("Customer ID:", customer.get("Customer ID"))
print("Customer Name:", customer.get("Customer Name"))
print("Age:", customer.get("Age"))
print("Account Type:", customer.get("Account Type"))
print("Branch:", customer.get("Branch"))
print("Phone Number:", customer.get("Phone Number"))
print("Email:", customer.get("Email"))

print("\nDeposit Amount:", deposit)
print("Withdrawal Amount:", withdrawal)
print("Final Balance:", customer.get("Balance"))

if customer.get("Balance") > 0:
    print("Account Status: Active")
else:
    print("Account Status: Inactive")