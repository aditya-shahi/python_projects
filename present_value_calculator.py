# Accept the inputs

startbalance = float(input("Enter the future amount received: "))
years = int(input("Enter the number of years: "))
rate = float(input("Enter the discounting interest rate: "))

rate = rate/100

total_interest = 0.0

# Display the header for the table

print("%4s%18s%10s%16s" % \
	("Year", "Starting Balance", "Interest", "Ending Balance"))

# Compute and display the results for each year

for year in range (1, years+1):
	interest = startbalance - (startbalance/(1+rate))
	endbalance = startbalance - interest
	print("%4d%18.2f%10.2f%16.2f" % \
		(year, startbalance, interest, endbalance))

	startbalance = endbalance
	total_interest += interest  

# Display the totals for the period
print("Ending balance: $%0.2f" % endbalance)
print("Total interest earned: $%0.2f" % total_interest)