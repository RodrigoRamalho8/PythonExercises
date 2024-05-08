#Here we use float because our main theme is money, and we always expect to have decimals
hourlyPay = float(input("Enter your hourly wage: "))
hoursWorkedPerDay = int(input("How much hours have you worked per day: "))
daysInMonth = int(input("Number of days on month: "))

wage = hourlyPay * hoursWorkedPerDay * daysInMonth

#Again we format using ":.2f"
print(f'Total wage: ${wage:.2f}')
