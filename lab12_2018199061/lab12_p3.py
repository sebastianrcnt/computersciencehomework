# import modules
import random

# characters that consist input files
alphabet_bank = list('abcdefghijklmnopqrstuvwxyz')
digit_bank = list('0123456789')
character_bank = alphabet_bank + digit_bank

# functions
def generateKey():
    keyDict = {}
    character_bank_copy = character_bank[:]
    for key_character in character_bank:
        value_character = random.choice(character_bank_copy)
        character_bank_copy.remove(value_character)
        keyDict[key_character] = value_character
    return keyDict


def encryptText(text, keyDict):

# Init
# get filename and its extension
filename = input('Enter a filename: ')
extension = filename.split('.')[-1]

if extension == 'txt':
    # open files
    txt_file = open(filename, 'r')
    enc_file = open(filename, 'w')
    text = txt_file.read()
    # encrypt

    # close files
    txt_file.close()
    enc_file.close()
elif extension == 'enc':
    pass