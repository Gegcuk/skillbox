def ex20_1_1():
    # Задача 1. Словарь квадратов чисел
    # На вход программе поступает целое число num. Напишите программу создания словаря, который включает в себя ключи
    # от 1 до num, а значениями соответствующего ключа будет значение ключа в квадрате.
    #
    # Пример:
    # Введите целое число: 5
    #
    # Результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    user_number = int(input('Enter your number: '))
    result_dict = {}
    for i_num in range(user_number):
        result_dict[i_num + 1] = (i_num + 1) ** 2
    print(result_dict)


def ex20_1_2():
    # Задача 2. Студент
    # Пользователь вводит фамилию, имя студента, город проживания, вуз, в котором он учится, и все его оценки.
    # Всё вводится в одну строку через пробел. Напишите программу, которая по этой информации составит словарь и выведет его на экран.
    #
    # Пример:
    # Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки): Илья Иванов Москва МГУ 5 4 4 4 5
    #
    # Результат:
    # Имя - Илья
    # Фамилия - Иванов
    # Город - Москва
    # Место учёбы - МГУ
    # Оценки - [5, 4, 4, 4, 5]
    student_info = input('Enter information about student: ').split()
    student_info_dict = dict()
    student_info_dict['Name'] = student_info[0]
    student_info_dict['Second name'] = student_info[1]
    student_info_dict['City'] = student_info[2]
    student_info_dict['College'] = student_info[3]
    student_info_dict['Marks'] = []
    for i_grade in student_info[4:]:
        student_info_dict['Marks'].append(int(i_grade))
    print(student_info_dict)
