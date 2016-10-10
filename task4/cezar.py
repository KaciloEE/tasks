def code(str,key):
  s = []
  for letter in str:
    s+="".join(chr(ord(letter)+key))
  return(s)

print("".join(code("Test",2)))
