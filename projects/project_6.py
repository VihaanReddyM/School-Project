
principal_amount = float(input("Enter the principal amount in thousand: "))

rate_of_interest = float(input("Enter the rate of interest (e.g., 6.5): "))

time_in_years = float(input("Enter the time in years: "))

simple_interest = (principal_amount * rate_of_interest * time_in_years) / 100

print("Data Type of Principal Amount:", type(principal_amount))
print("Data Type of Rate of Interest:", type(rate_of_interest))
print("Data Type of Time in Years:", type(time_in_years))
print("Data Type of Simple Interest:", type(simple_interest))

print("Simple Interest:", simple_interest)
