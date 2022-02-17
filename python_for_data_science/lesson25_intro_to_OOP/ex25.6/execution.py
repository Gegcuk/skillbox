import random
from students import Student

students_list = [Student('Bob', random.randint(1, 5), [random.randint(10, 100) for _ in range(5)]) for _ in range(10)]

print(sorted([student.average_mark() for student in students_list]))