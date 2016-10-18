def capitalization(a,b,c):
  return(
    a*(1+(b/100)*(c/12))
  )


money = capitalization(10000,10,2)

print(round(money))
