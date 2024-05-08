num = int(input("Enter a number for our multiplication table: "))

table = [0,1,2,3,4,5,6,7,8,9,10]

#The loop for do what we need every time it repeat, so it is showing us our number times every element in "table" list
for i in table:
	result = num*i
	print(f'{num} x {i} = {result}')
	
