<<<<<<< HEAD
def capitalization(a,b,c):
  return(
    a*(1+(b/100)*(c/12))
  )


money = capitalization(10000,10,2)
=======
def capitalization(a, b, c):
    return(
        a * (1 + (b / 100) * (c / 12))
    )


money = capitalization(10000, 10, 2)
>>>>>>> 7043ebe108d4468dd6cb30e4f503e22f3be429f9

print(round(money))
