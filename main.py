numGrades = int(input('How many grades do you have: '))
grades = []
bucket = 0
for i in range(0, numGrades, 1):
    grade = float(input('Please input your grades: '))
    grades.append(grade)
    print(grades)
print('Your grades are: ')
for i in range(0, numGrades, 1):
    print(grades[i])
for i in range(0, numGrades, 1):
    bucket = bucket + grades[i]
average = bucket / numGrades
print('')
print('Your average is: ', average)


