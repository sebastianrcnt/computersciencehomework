# import modules
import random
from copy import deepcopy
# assign bank of characters that consist input files
alphabet_bank = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
digit_bank = list('0123456789')
space = list(' ')
character_bank = alphabet_bank + digit_bank + space

# functions
def generateKey():
    """
    generate random key dictionary

    :return: key_dict (dictionary)
    """
    key_dict = {}
    character_bank_copy = deepcopy(character_bank)

    # choose a value for each key character
    for key_character in character_bank:
        # chose one character from copy of character bank
        value_character = random.choice(character_bank_copy)
        # remove it from character bank copy
        character_bank_copy.remove(value_character)
        # add key value pair to key_dict
        key_dict[key_character] = value_character

    # return generated key dictionary
    return key_dict

def encryptText(text, key_dict):
    """
    encrypts text with key dictionary and return the encrypted text

    :param text: (string) text for encrypting
    :param key_dict: (dictionary) keys dictionary
    :return: enc_text (string) encrypted text
    """
    enc_text = ''

    # encrypt each character
    for char in text:
        # do not encrypt newline character('\n')
        if char == '\n':
            enc_char = char
        else:
            enc_char = key_dict[char]
        enc_text = enc_text + enc_char

    # return encrypted text
    return enc_text

def decryptText(text, key_dict):
    """
    decrypts text with key dictionary and return the decrypted text

    :param text: (string) text for decrypting
    :param key_dict: (dictionary) keys dictionary
    :return: dec_text (string) decrypted text
    """

    # generate a reversed key dictionary(keys will be values and vice versa)
    key_dict_reversed = {}
    for key in key_dict.keys():
        value = key_dict[key]
        # assert value not in key_dict_reversed.keys()
        key_dict_reversed[value] = key

    # decrypt each character
    dec_text = ''
    for char in text:
        if char == '\n':
            dec_char = char
        else:
            dec_char = key_dict_reversed[char]
        dec_text = dec_text + dec_char

    # return decrypted text
    return dec_text

def make_csv(key_dict):
    """
    generate a csv text from a given key dictionary

    :param key_dict: (dict) key dictionary
    :return: csv_text (string)
    """
    csv_text = ''
    # write each line
    for key in key_dict:
        csv_text = csv_text + key + ',' + key_dict[key] + '\n'
    # return csv_text without the last newline character.
    # newline character at the end of csv_text could cause errors when parsing them back to a dictionary.
    return csv_text[:-1]

def parse_csv(csv_text):
    """
    parse a csv text back to a key dictionary

    :param csv_text: (string) csv text to parse
    :return: (dictionary) parsed dictionary
    """
    key_dict = {}
    # each line is a pair, so split with newline character
    csv_pairs = csv_text.split('\n')
    # add each pair to key dictionary
    for pair in csv_pairs:
        key = pair.split(',')[0]
        value = pair.split(',')[1]
        key_dict[key] = value
    # return the generated key dictionary
    return key_dict

# Init
# get filename and its extension
filename = input('Enter a filename: ')

# split filename into its name and extension (foo.txt -> foo, txt)
last_dot_index = None

# last appearing dot is the splitter (since file names could contain multiple dots)
for i in range(len(filename)):
    if filename[i] == '.':
        # reassign last_dot_index
        # at the end of this loop, the index of the last dot will be assigned
        last_dot_index = i

# split filename
extension = filename[last_dot_index+1:]
filename_without_extension = filename[:last_dot_index]

# when filename has txt extension
if extension == 'txt':
    # open files
    txt_file = open(filename, 'r')
    enc_file = open(filename_without_extension + '.enc', 'w')
    key_file = open(filename_without_extension + '.key', 'w')

    # read content of txt_file
    txt_text = txt_file.read()

    # encrypt
    encrypt_key = generateKey()
    encryped_text = encryptText(txt_text, encrypt_key)

    # write enc file
    enc_file.write(encryped_text)

    # write key file
    csv_text = make_csv(encrypt_key)
    key_file.write(csv_text)

    # close files
    txt_file.close()
    enc_file.close()
    key_file.close()

# when filename has enc extension
elif extension == 'enc':
    # open files
    txt_file = open(filename_without_extension + '.txt', 'w')
    enc_file = open(filename, 'r')
    key_file = open(filename_without_extension + '.key', 'r')

    # read content of enc_file, key_file
    enc_text = enc_file.read()
    key_text = key_file.read()

    # parse key_text
    key_dict = parse_csv(key_text)

    # decrypt enc_text
    dec_text = decryptText(enc_text, key_dict)

    # write dec_text to txt_file
    txt_file.write(dec_text)

    # close all files
    txt_file.close()
    enc_file.close()
    key_file.close()
