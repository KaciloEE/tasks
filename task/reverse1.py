def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1
        new_strings.append(a_string[index])
    return ''.join(new_strings)

<<<<<<< HEAD
=======

>>>>>>> 7043ebe108d4468dd6cb30e4f503e22f3be429f9
print(reverse_a_string_more_slowly('ecnalubma'))
