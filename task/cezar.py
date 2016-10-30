def code(str,key):
  return ["".join(chr(ord(letter)+key)) for letter in str ]

print("".join(code("Test",2)))
