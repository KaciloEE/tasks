def st(a,b):
    if type(a) == str or type(b) == str:
        return 'получена строка'
    if type(a) == int and type(b) == int:
        if int(a) > int(b):
            return 'больше'
        elif int(a) == int(b):
            return 'равны'
        elif int(a) < int(b):
            return 'меньше'

print(st(3,7))
