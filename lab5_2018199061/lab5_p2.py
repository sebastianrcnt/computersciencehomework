ans = input('Enter a sentence: ')
output = ans.count('a') + ans.count('e') + ans.count('i') + ans.count('o') + ans.count('u') + ans.count('A') + ans.count('E') + ans.count('I') + ans.count('O') + ans.count('U')
if output == 1:
    print(f"Your sentence contains {output} vowel.")
else:
    print(f"Your sentence contains {output} vowels.")
