ans = input('Enter a sentence: ') # get user input
output = ans.count('a') + ans.count('e') + ans.count('i') + ans.count('o') + ans.count('u') + ans.count('A') + ans.count('E') + ans.count('I') + ans.count('O') + ans.count('U') # count every vowel and add up the number of appearances
if output == 1: # singular
    print(f"Your sentence contains {output} vowel.")
else: # plural
    print(f"Your sentence contains {output} vowels.")
