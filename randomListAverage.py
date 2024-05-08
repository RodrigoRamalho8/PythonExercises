import random

listlen = int(input("Enter the length of our list: "))
randomList = []

for i in range(1,listlen+1):
	i = random.randint(1,100)
	randomList.append(i)
	
sumList = sum(randomList)
result = sumList/len(randomList)

print(f'Our list {randomList} have {len(randomList)} element/s resulting in: {result:.2f}')
