principal_amount_in_rupees = float(input("Enter principal amount in rupees: "))
rate_of_interest_in_percent = float(input("Enter rate of interest in percent: "))
time_in_years = float(input("Enter time in years: "))

total_amount_in_rupees = principal_amount_in_rupees * (1 + rate_of_interest_in_percent / 100) ** time_in_years

compound_interest_in_rupees = total_amount_in_rupees - principal_amount_in_rupees

print(f"Total amount is {total_amount_in_rupees} rupees")
print(f"Compound interest is {compound_interest_in_rupees} rupees")
