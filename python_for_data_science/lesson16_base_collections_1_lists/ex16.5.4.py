# Задача 4. Видеокарты
#
# Что нужно сделать
# В базе магазина электроники есть список видеокарт компании NVIDIA разных поколений. Вместо полных названий хранятся
# только числа, которые обозначают модель и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт.
# Самые старшие поколения разобрали за пару дней.
#
# Напишите программу, которая удаляет списка видеокарт наибольшие элементы.# #
# Пример:
#
# Количество видеокарт: 5#
# 1 Видеокарта: 3070#
# 2 Видеокарта: 2060#
# 3 Видеокарта: 3090#
# 4 Видеокарта: 3070#
# 5 Видеокарта: 3090#
#
# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
#
# Новый список видеокарт: [ 3070 2060 3070 ]#


def delete_max_elements(list_for_deleting):
    max_value = max(list_for_deleting)
    list_without_max_elements = []
    for i in range(len(list_for_deleting)):
        if list_for_deleting[i] < max_value:
            list_without_max_elements.append(list_for_deleting[i])
    return list_without_max_elements


GPUCOunt = int(input("Insert count of GPUs: "))
GPUList = []
NewGPUList = []
for _ in range(GPUCOunt):
    GPUList.append(int(input("GPU: ")))

NewGPUList = delete_max_elements(GPUList)

print(GPUList)
print(NewGPUList)