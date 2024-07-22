# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

grades = [(5 + 3 + 3 + 5 + 4)/5], [(2 + 2 + 2 + 3)/4], [(4 + 5 + 5 + 2)/4], [(4 + 4 + 3)/3], [(5 + 5 + 5 + 4 + 5)/ 5]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# 1 вариант
cr_znach = {'Johnny': grades[0], 'Bilbo': grades[1], 'Steve': grades[2], 'Khendrik':grades[3], 'Aaron':grades[4]}
print(cr_znach)

# 2 вариант

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
grades_m = sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])
dict1 = {students[0]: grades_m[0], students[1]: grades_m[1], students[2]:grades_m[2], students[3]: grades_m[3], students[4]: grades_m[4]}
print(dict1)

# 3 вариант

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort = sorted(students)
grades_m = []

for num in grades:
    s = sum(num)/len(num)
    grades_m.append(s)

#print(students_sort)
#print(grades_m)
dict1 = dict(zip(students_sort, grades_m))
print(dict1)
