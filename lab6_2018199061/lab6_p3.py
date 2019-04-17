# Password Encryption/Decryption Program
# Import modules
import sys

# init
password_out = ''
case_changer = ord('a') - ord('A')
encryption_key = (('a', 'm'), ('b', 'h'), ('c', 't'), ('d', 'f'), ('e', 'g'),
                  ('f', 'k'), ('g', 'b'), ('h', 'p'), ('i', 'j'), ('j', 'w'), ('k', 'e'), ('l', 'r'),
                  ('m', 'q'), ('n', 's'), ('o', 'l'), ('p', 'n'), ('q', 'i'), ('r', 'u'), ('s', 'o'),
                  ('t', 'x'), ('u', 'z'), ('v', 'y'), ('w', 'v'), ('x', 'd'), ('y', 'c'), ('z', 'a'),
                  ('#', '!'), ('@', '('), ('%', ')'))

encrypting = True
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
non_alphabet = '#@%'
digit = '0123456789'


# get password
password_in = input('Enter password: ')

# Check whether password is valid
counter = [0, 0, 0]  # [alphabet, non-alphabet, digit]

# Count appearences of alphabet, non alphabet, and digit
# Reject when there is one or more character that is not among them.
for i in password_in:
    if i in alphabet:
        counter[0] = counter[0] + 1
    elif i in non_alphabet:
        counter[1] = counter[1] + 1
    elif i in digit:
        counter[2] = counter[2] + 1
    else:  # if the character belongs nowhere
        print('Invalid password!')
        sys.exit()  # reject

# Check that every password contains at least one letter, non-alphabetic character, and digit.
if (counter[0] == 0) or (counter[1] == 0) or (counter[2] == 0):
    print('Invalid password!')  # reject
    sys.exit()

# perform encryption / decryption
if encrypting:
    from_index = 0
    to_index = 1
else:
    from_index = 1 
    to_index = 0

case_changer = ord('a') - ord('A')
    
for ch in password_in:
    letter_found = False
    
    for t in encryption_key:
        if ('a' <= ch <= 'z') and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
        elif ('A' <= ch <= 'Z') and chr(ord(ch) + 32) == t[from_index]:
            password_out = password_out + chr(ord(t[to_index]) - case_changer)
            letter_found = True
            
    if not letter_found:
        password_out = password_out + ch
            
# output
if encrypting:
    print('Your encrypted password is:', password_out)
else:
    print('Your decrypted password is:', password_out)
