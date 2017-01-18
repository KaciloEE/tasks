'''
Факториалом числа называют произведение всех натуральных чисел до него включительно. Например, факториал числа 5 равен произведению 1*2*3*4*5 = 120. Формулу нахождения факториала можно записать следующим образом: n! = 1 * 2 * … * n, где n – это число, а n! – факториал этого числа.
Можно записать немного по-другому: n! = 1 * … * (n-2) * (n-1) * n, т.е. каждое предыдущее число меньше на единицу, чем последующее. Нахождение факториала числа по первой формуле можно реализовать с помощью цикла while, а по второй формуле – с помощью рекурсии.
'''

def factorial(n):
    fac = 1
    i = 0
    while i < n:
        i += 1
        fac = fac * i
    return fac

print(factorial(5))

'''
Первых проход по телу цикла while свяжет переменную fac с произведением 1 * 1. Второй - 1 * 2, затем 2 * 3, 6 * 4, 24 * 5. Шестой раз цикл while выполняться не будет, т.к. значение переменной i будет равно 5 и выражение i < n вернет false.
'''