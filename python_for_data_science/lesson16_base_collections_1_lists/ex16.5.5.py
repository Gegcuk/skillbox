# Задача 5. Кино
#
# Что нужно сделать
# Илья зашёл на любительский киносайт, на котором пользователи оставляют рецензии на фильмы. Их список:
#
# films = [‘Крепкий орешек’, ‘Назад в будущее’, ‘Таксист’, ‘Леон’, ‘Богемская рапсодия’, ‘Город грехов’, ‘Мементо’, ‘Отступники’, ‘Деревня’]
#
# Илья на сайте в первый раз. Он хочет зарегистрироваться и сразу добавить часть фильмов в список любимых, чтобы позже прочитать рецензии на них.
#
# Напишите программу, в которой пользователь вводит фильм. Если он есть в перечне, то добавляется в список любимых. Если его нет, то выводится ошибка. В конце выведите весь список любимых фильмов.
# #
# Пример:
#
# Сколько фильмов хотите добавить? 3#
# Введите название фильма: Леон#
# Введите название фильма: Безумный Макс#
# Ошибка: фильма Безумный Макс у нас нет :(#
# Введите название фильма: Мементо#
# Ваш список любимых фильмов: Леон, Мементо


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite_films = []
counts_of_favorite_films = int(input("How many films do you want to add?: "))
for _ in range(counts_of_favorite_films):
    film = input("Insert film`s title: ")
    if film in films:
        favorite_films.append(film)
        continue
    else:
        print('Фильма {} у нас нет =('.format(film))

print('Ваш список любимых фильмов: {}'.format(', '.join(favorite_films)))
