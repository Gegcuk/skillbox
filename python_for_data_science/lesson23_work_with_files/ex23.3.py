def ex23_3_1():
    # Задача 1. Результаты
    #
    # Одному программисту дали задачу для обработки неких результатов тестирования двух групп людей. Файл
    # первой группы (group_1.txt) находится в папке task, файл второй группы (group_2.txt) — в папке Additional_info.
    #
    # На экран нужно было вывести сумму очков первой группы, затем разность очков опять же первой группы и
    # напоследок — произведение очков уже второй группы.
    file1 = open('test_text_file_1.txt', 'r', encoding='utf-8')
    file2 = open('text_text_file_2.txt', 'r', encoding='utf-8')
    first_team_sum = 0
    first_team_diff = 0
    second_team_mult = 1
    for line in file1:
        first_team_diff += int(line.split()[2])
        first_team_sum -= int(line.split()[2])
    for line in file2:
        second_team_mult *= int(line.split()[2])
    file2.close()
    file1.close()
    print(f'First team sum: {first_team_sum}')
    print(f'First team diff: {first_team_diff}')
    print(f'Second team mult: {second_team_mult}')


