# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# tmap = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? Column then row: ")

# column = int(position[0])
# row = int(position[1]) 
# tmap[row -1][column -1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")
# import random
# char_list = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
# pass_length = int(input("What is your desired password length?"))
# password = ''.join(random.choice(char_list) for _ in range(pass_length)) 
# print(password)
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

summ = 0
count = 0

for num in student_heights:
    summ += num
    count += 1
average = summ / count

print(round(average))
