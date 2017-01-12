def ticket_type(t):
  n1 = t[0:3]
  n2 = t[3:]
  summa1 = sm(n1)
  summa2 = sm(n2)
  var1 = ''
  if summa1 == summa2:
    var1 = 'Счастливый'
  elif  (summa1-summa2) == 1 or (summa2-summa1) == 1:
    var1 = "Встречный"
  elif (summa1-summa2) == 2 or (summa2-summa1) == 2:
    var1 = "Пьяный"
  else:
    var1 = "Обычный"

  return (var1)


def sm(c):
  summa11 = 0
  for i in c:
    summa11 +=int(i)
  return summa11

result = ticket_type("123321")
print(result)

