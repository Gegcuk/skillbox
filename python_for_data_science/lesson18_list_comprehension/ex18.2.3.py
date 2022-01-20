# Дан список цен на пять товаров с точностью до копейки. Так как экономика даёт о себе знать, мы спрогнозировали, что через год придётся повышать цены на X процентов, а ещё через один год — ещё на Y процентов.
#
# Напишите программу, которая получает на вход список цен на товары (вещественные числа, список генерируется также с помощью list comprehensions) и выводит в одну строку общую сумму стоимости товаров за каждый год.
#
#
#
# Пример:
#
# Цена на товар: 1.09
#
# Цена на товар: 23.56
#
# Цена на товар: 57.84
#
# Цена на товар: 4.56
#
# Цена на товар: 6.78
#
# Повышение на первый год: 0
#
# Повышение на второй год: 10
#
# Сумма цен за каждый год: 93.83 93.83 103.22

def get_list_of_increased_price(list_for_increase, percent):
    return [round(x * (1 + percent/100), 2) for x in list_for_increase]


price_list = [round(float(input("Product price: ")), 2) for _ in range(0, 5)]
first_increase = int(input("First year increase: "))
second_year_increase = int(input("Second year increase: "))

first_year_price_list = get_list_of_increased_price(price_list, first_increase)
second_year_price_list = get_list_of_increased_price(first_year_price_list, second_year_increase)

print(first_year_price_list)
print(second_year_price_list)