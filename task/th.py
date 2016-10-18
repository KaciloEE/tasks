import decimal

n = '12345678'
x = decimal.Decimal(n)

print('{0:,}'.format(x).replace(',',' '))
