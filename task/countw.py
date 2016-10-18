s = []
i = Word = 0
String = "Мы с Андреем пошли на рыбалку , а затем вернулись домой !"
while i < len(String): # Добавляем каждый элемент из строки
    s.append(String[i])
    i += 1

i = 0
if ( s[0] != ' ' ): # Проверка если массив начинается со слова
       Word = 1
while i < len(String)-1: # Считаем слова
    if ( s[i] == ' ') and ( s[i+1] != ',') and ( s[i+1] != '!'):
        Word += 1
    i += 1

print (Word)

