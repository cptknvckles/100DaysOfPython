# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#dont use max() or min() 
x = 0
y = 0
for check in student_scores:
    x = check
    if x > y:
        y = check
print(f"The highest score in class is: {y}")
summ = 0
count = 0

for num in student_scores:
    summ += num
    count += 1
average = summ / count
print('And the average score is: ' + str(round(average)))
#45 50 60 80 92 65
'''
placing each number(check) into new var x
need to check if x is higher than the next number
if it is keep that number in x and then print out the winner




'''