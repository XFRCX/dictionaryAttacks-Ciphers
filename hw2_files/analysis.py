from collections import OrderedDict
import collections
import string

#function that returns the frequency of characters in cipher text in a dictinary
def frequency(cipher_text):
    letter_Frequency = {}
    for letter in cipher_text:
        if letter in letter_Frequency:
            letter_Frequency[letter] += 1
        else:
            letter_Frequency[letter] = 1
    ord_letter_frequency = OrderedDict(sorted(letter_Frequency.items()))
    return ord_letter_frequency

#function used to print plain text of cipher text
def decode(cipher_text, alphaKey):
    print(cipher_text.translate(str.maketrans(alphaKey, string.ascii_lowercase)))





cipher_text = input("Please enter the text to decipher\n")
letter_Frequency = frequency(cipher_text)
alphabet = ""
#make a string of all the character found in the cipher text
for i in letter_Frequency:
    alphabet = ''.join(alphabet + i)

print("\n\n-----Characters found in Cipher text------\n")
print("\t{}".format(alphabet))
print("------------------------------------------\n")


print("---------***Frequency Analysis***---------\n")
for key in letter_Frequency:
    print("\t {} found {} ".format(key, letter_Frequency[key]))
print("------------------------------------------\n")

print("----Characters not found in cipher text---\n")
for chr in string.ascii_lowercase:
    if chr not in letter_Frequency :
        print("\t ----> {}".format(chr))
print("------------------------------------------\n")



#alphabet mapping found after manully messing around with different mappings
alphaKey = "sgquntivdaejrozhpyfclwxmkb"
print("-----------The alphabet mapping-----------")
for cipherChar, plainChar in zip(alphaKey, string.ascii_lowercase):
    print("\t {} ----> {}".format(cipherChar, plainChar))
print("------------------------------------------\n")

print("-----------cipher text to plain text------\n")
decode( cipher_text, alphaKey)
print("\n------------------------------------------\n")


'''The following are muliple attempts of manually trying to figure out the alphabet mapping'''
'''there are shown to show my work'''
# sub = cipher_text.replace("l", "\033[33mu\033[0m")
# sub = sub.replace("j", "\033[33ml\033[0m")
# sub = sub.replace("b", "\033[33mj\033[0m")
# sub = sub.replace("g", "\033[33mb\033[0m")
# sub = sub.replace("i", "\033[33mg\033[0m")
# sub = sub.replace("d", "\033[33mi\033[0m")
# sub = sub.replace("u", "\033[33md\033[0m")
# # sub = sub.replace("l", "\033[33mu\033[0m")
# # sub = sub.replace("j", "\033[33ml\033[0m")
#
# # sub = sub.replace("b", "\033[33mj\033[0m")
#
# # sub = sub.replace("g", "\033[33mb\033[0m")
# # sub = sub.replace("i", "\033[33mg\033[0m")
# # sub = sub.replace("d", "\033[33mi\033[0m")
# sub = sub.replace("s", "\033[33ma\033[0m")
# #(*)
# sub = sub.replace("f", "\033[33ms\033[0m")
# sub = sub.replace("t", "\033[33mf\033[0m")
# #c can't be e so we'll switch e and t the two highest frequencies
# sub = sub.replace("c", "\033[33mt\033[0m")
# sub = sub.replace("r", "\033[33mm\033[0m")
# #next in my list y to r
# sub = sub.replace("y", "\033[33mr\033[0m")
# sub = sub.replace("k", "\033[33my\033[0m")
# sub = sub.replace("e", "\033[33mk\033[0m")#--
#
#
# sub = sub.replace("n", "\033[33me\033[0m")
# #next in the list o match to n
# sub = sub.replace("o", "\033[33mn\033[0m")
# #switch frequencies o and i to match d match with i
# sub = sub.replace("z", "\033[33mo\033[0m")
# #note o and z had to be switch to avoid overwritten values
# #next in the list is v to h
# # sub = sub.replace("h", "\033[33mp\033[0m")#
# #sub = sub.replace("v", "\033[33mh\033[0m")
#
# #next was u to r but I noticed that it could not be possible, u to d was possible so I chose that
# # sub = sub.replace("u", "\033[33md\033[0m")
# #through analyzing i noticed that f to s could resolve some words
# #sub = sub.replace("f", "\033[33ms\033[0m")
# #(*)sub = sub.replace("b", "\033[33mj\033[0m")
#
# #(*)
# # sub = sub.replace("u", "\033[33md\033[0m")
# # sub = sub.replace("l", "\033[33mu\033[0m")
# # sub = sub.replace("j", "\033[33ml\033[0m")
# # sub = sub.replace("w", "\033[33mv\033[0m")
# # sub = sub.replace("x", "\033[33mw\033[0m")
# #sub = sub.replace("m", "\033[33mx\033[0m")
#
# #thorugh analyzing i to g and w to v could resolve more words but i had to put the
# #in a certain way to not overwrite was was already fixed (*) --indicates place
# sub = sub.replace("q", "\033[33mc\033[0m")
# sub = sub.replace("p", "\033[33mq\033[0m")
# sub = sub.replace("h", "\033[33mp\033[0m")#
# sub = sub.replace("v", "\033[33mh\033[0m")
# sub = sub.replace("w", "\033[33mv\033[0m")
# sub = sub.replace("x", "\033[33mw\033[0m")


#sub = sub.replace('m,', 'x')

# #------------



# sub = cipher_text.replace("b", "z")# b- j
# sub = cipher_text.replace("v", "h")
# sub = sub.replace("w", "v")
# sub = sub.replace("x", "w")
# sub = sub.replace("m", "x")
# sub = sub.replace("r", "m")
# sub = sub.replace("y", "r")
# sub = sub.replace("k", "y")
# sub = sub.replace("e", "k")
# sub = sub.replace("n", "e")
# sub = sub.replace("o", "n")
# sub = sub.replace("z", "o")
# sub = sub.replace("g", "b")
# sub = sub.replace("i", "g")
# sub = sub.replace("d", "i")
#sub = sub.replace("l", "u")#--
# sub = sub.replace("u", "d")
# sub = sub.replace("l", "u")#--
# sub = sub.replace("j", "l")
# sub = sub.replace("s", "a")
# sub = sub.replace("f", "s")
# sub = sub.replace("t", "f")
# sub = sub.replace("c", "t")
# sub = sub.replace("q", "c")
# sub = sub.replace("p", "q")
# sub = sub.replace("h", "p")
# sub = sub.replace("v", "h")
# sub = sub.replace("w", "v")
# sub = sub.replace("x", "w")
# sub = sub.replace("m", "x")
# sub = sub.replace("r", "m")
# sub = sub.replace("y", "r")
# sub = sub.replace("k", "y")
# sub = sub.replace("e", "k")
# sub = sub.replace("n", "e")
# sub = sub.replace("o", "n")
# sub = sub.replace("z", "o")
#sub = sub.replace("b", "z")
# sub = sub.replace("a", "z")



'''----------------------------------------'''
# sub = cipher_text.replace("m", "\033[33mx\033[0m")
# sub = sub.replace("r", "\033[33mm\033[0m")
# sub = sub.replace("y", "\033[33mr\033[0m")
# sub = sub.replace("k", "\033[33my\033[0m")
# sub = sub.replace("e", "\033[33mk\033[0m")
# sub = sub.replace("n", "\033[33me\033[0m")
# sub = sub.replace("o", "\033[33mn\033[0m")
# sub = sub.replace("z", "\033[33mo\033[0m")
# sub = sub.replace("a", "\033[33mz\033[0m")
# sub = sub.replace("s", "\033[33ma\033[0m")
# sub = sub.replace("f", "\033[33ms\033[0m")
# sub = sub.replace("t", "\033[33mf\033[0m")
# sub = sub.replace("c", "\033[33mt\033[0m")
# sub = sub.replace("q", "\033[33mc\033[0m")
# sub = sub.replace("p", "\033[33mq\033[0m")
# sub = sub.replace("h", "\033[33mp\033[0m")
# sub = sub.replace("v", "\033[33mh\033[0m")
# sub = sub.replace("w", "\033[33mv\033[0m")
# sub = sub.replace("x", "\033[33mw\033[0m")
# sub = sub.replace("u", "\033[33md\033[0m")
# sub = sub.replace("l", "\033[33mu\033[0m")
# sub = sub.replace("b", "\033[33mj\033[0m")
# sub = sub.replace("g", "\033[33mb\033[0m")
# sub = sub.replace("i", "\033[33mg\033[0m")
# sub = sub.replace("d", "\033[33mi\033[0m")
# sub = sub.replace("u", "\033[33md\033[0m")

'''----------------------------------------'''



'''----------------------------------------'''
# sub = cipher_text.replace("a", "z")
# sub = sub.replace("b", "j")
# sub = sub.replace("c", "t")
# sub = sub.replace("d", "i")
# sub = sub.replace("e", "k")
# sub = sub.replace("f", "s")
# sub = sub.replace("g", "b")
# sub = sub.replace("h", "p")
# sub = sub.replace("i", "g")
# sub = sub.replace("j", "l")
# sub = sub.replace("k", "y")
# sub = sub.replace("l", "u")
# sub = sub.replace("m", "x")
# sub = sub.replace("n", "e")
# sub = sub.replace("o", "n")
# sub = sub.replace("p", "q")
# sub = sub.replace("q", "c")
# sub = sub.replace("r", "m")
# sub = sub.replace("s", "a")
# sub = sub.replace("t", "f")
# sub = sub.replace("u", "d")
# sub = sub.replace("v", "h")
# sub = sub.replace("w", "v")
# sub = sub.replace("x", "w")
# sub = sub.replace("y", "r")
# sub = sub.replace("z", "o")
#print(sub)
'''----------------------------------------'''
