number = int(input('Insert number: '))

summa = 0

while number != 0:
    last_num = number % 10
    summa += last_num
    if last_num == 5:
        print('Gap detected')
        break
    number //= 10
print('\n total sum: ', summa)
print('Finish')

