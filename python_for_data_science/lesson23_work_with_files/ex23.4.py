# Во входном файле numbers.txt записано N целых чисел, каждое в отдельной строке. Напишите программу,
# которая выводит их сумму в выходной файл answer.txt.

file = open('numbers.txt', 'r', encoding='utf-8')
sum = 0
for line in file:
    sum += int(line)

file_for_answer = open('answer.txt', 'a')
sum = str(sum) + '\n'
file_for_answer.write(str(sum))

file.close()
file_for_answer.close()
