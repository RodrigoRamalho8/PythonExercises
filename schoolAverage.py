#This program will receive 3 grades and return the average between it
grade1 = int(input("Enter the first grade: "))
grade2 = int(input("Enter the second grade: "))
grade3 = int(input("Enter the third grade: "))

#Here we create another variable to calculate the average and be easier to concatenate
average = (grade1+grade2+grade3)/3

#Using f'' on print we can concatenate variables while in the text by inserting it inside {}, we can also use :.2f showing a limit for decimals
print(f'School average: {average:.2f}')
