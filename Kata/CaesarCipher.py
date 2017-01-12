class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift;

    def encode(self, str):
        dict = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        dict_len = len(dict)

        res = ''
        str = str.lower()
        for i in str:
            if i in dict:
                tmp = (dict.index(i) + self.shift) % dict_len
                res = res + dict[tmp]
            else:
                res =res + i
        return res.upper()

    def decode(self, str):
        dict = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        dict_len = len(dict)

        res = ''
        str = str.lower()
        for i in str:
            if i in dict:
                tmp = (dict.index(i) - self.shift) % dict_len
                res = res + dict[tmp]
            else:
                res =res + i
        return res.upper()


c = CaesarCipher(5);

print(c.encode('Codewars'))
print(c.decode('HTIJBFWX'))
#'HTIJBFWX'

