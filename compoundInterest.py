#Formula: A = (P*(1+i)^n), where A is the amount, P is the principal, i is the annual interest rate, and n is the number of periods.

P = float(input("Enter the principal amount: "))
i = float(input("Enter the annual interest rate(Only number): "))
i = i/100 
n = float(input("Enter the number of period(In years): "))

A = P*(1+i)**n

print(f'The amount after {int(n)} year(s) will be: ${A:.2f}')


