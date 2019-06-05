# welcome
print('This program can determine if a given string is a palindrome\n')
print('(Enter return to exit)')

# get string from user
chars = input('Enter string to check: ')

while chars != '':
    isPalindrome = True

    if len(chars) == 1:
        # if chars is one letter word, it is a palindrome
        print('A one letter word is by definition a palindrome\n')
    else:
        # check if the front half of chars matches the other half of chars.
        for i in range(len(chars) // 2):
            if chars[i] != chars[len(chars) - i - 1]:
                isPalindrome = False

        # display results
        if isPalindrome:
            print(chars, 'is a palindrome\n')
        else:
            print(chars, 'is NOT a palindrome\n')

    # get input
    chars = input('Enter string to check: ')