
# Создайте новую функцию def test... с произвольным числом параметров разного типа,
#   функция должна распечатывать эти  параметры внутри своего тела

def test(a, *, b = True, c="Строка", d, list_add = None):
    if list_add is None:
        list_add = ['Пустой лист']
    print(a, b, c, d, *list_add)
    print()

test(1, c = 3, d = 22.5)


# Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре
def factorialis_recursion(n):
    factorialis = 1

    if n > 1:
        factorialis = n * factorialis_recursion(n - 1)


    return factorialis

print(factorialis_recursion(14))


