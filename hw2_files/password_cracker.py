import hashlib
import itertools
import string
import collections

#notes--
#encode() converts the string into bytes to be accepted by hash function
#digest() returns the encoded data in byte format
#hexdigest() returns the encoded dat n hexadecimal format

def cipherUp(orginalString, key):
    lowerCaseAlphabetList = collections.deque(string.ascii_lowercase)
    lowerCaseAlphabetList.rotate(key)
    alphabetString = ''.join(list(lowerCaseAlphabetList))
    cipherString = orginalString.translate(str.maketrans(string.ascii_lowercase, alphabetString))
    return cipherString


#use md5 to try to crack the password size of 32 characters
def md5_hack_tool(passHash, SALT):
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')
        while word:
          if(SALT == "yes"):
              word = word + "SALT"
              print(word)
          hashedWord = hashlib.md5(word.encode('utf-8'))
          #print("comparing: {} to {} ".format(hashedWord.hexdigest(), passHash))
          if(hashedWord.hexdigest() == passHash):
            print("***Password was cracked using md5 hash algorithm***")
            print("password: {}".format(word))
            exit()
          word = fp.readline().strip('\n')
        fp.close()

#use sha1 to try to crack the password size of 40 characters
def sha1_hack_tool(passHash, SALT):
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')
        while word:
          word = word.replace('a', '4')
          word = word.replace('c', '(')
          word = word.replace('e', '3')
          word = word.replace('l', '1')
          word = word.replace('o', '0')
          word = word.replace('s', '5')
          hashedWord = hashlib.sha1(word.encode('utf-8'))
          print("comparing: {} to {} ".format(hashedWord.hexdigest(), passHash))
          if(hashedWord.hexdigest() == passHash):
            print("***Password was cracked using sha1 hash algorithm***")
            print("password: {}".format(word))
            exit()
          word = fp.readline().strip('\n')
        fp.close()

#use blake2s to try to crack the password size of 64 characters
def blake2s_hack_tool(passHash,SALT, CIPHER):
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')

        while word:
          if(SALT == "yes"):
             combinations = list(itertools.product([str(0),str(1),str(2),str(3),str(4),str(5),str(6),str(7),str(8), str(9)], repeat=5))
             string_list = map(''.join, combinations)
             for s in string_list:
                 cWord = word + s
                 print(cWord)
                 hWord = hashlib.blake2s(cWord.encode('utf-8'))
                 if(hWord.hexdigest() == passHash):
                   print("***Password was cracked using blake2s hash algorithm with SALT***")
                   print("password: {}".format(word))
                   exit()
          elif(CIPHER == "yes"):
              newWord = word
              for i in range(1, 26):
                  cipherWord = cipherUp(newWord, i)
                  print(cipherWord)
                  cHWord = hashlib.blake2s(cipherWord.encode('utf-8'))
                  if(cHWord.hexdigest() == passHash):
                    print("***Password was cracked using blake2s hash algorithm with cipher***")
                    print("password: {}".format(cipherWord))
                    exit()
          else:
            hashedWord = hashlib.blake2s(word.encode('utf-8'))
            #print("comparing: {} to {} ".format(hashedWord.hexdigest(), passHash))
            if(hashedWord.hexdigest() == passHash):
              print("***Password was cracked using blake2s hash algorithm***")
              print("password: {}".format(word))
              exit()

          word = fp.readline().strip('\n')
        fp.close()

#use sha256 to try to crack the password size of 64 characters
def sha256_hack_tool(passHash, SALT, CIPHER):
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')
        while word:
          if(SALT == "yes"):
              combinations = list(itertools.product([str(0),str(1),str(2),str(3),str(4),str(5),str(6),str(7),str(8), str(9)], repeat=5))
              string_list = map(''.join, combinations)
              for s in string_list:
                  cWord = word + s
                  print(cWord)
                  hWord = hashlib.sha256(cWord.encode('utf-8'))
                  if(hWord.hexdigest() == passHash):
                    print("***Password was cracked using sha256 hash algorithm with SALT***")
                    print("password: {}".format(word))
                    exit()

          elif(CIPHER == "yes"):
              newWord = word
              for i in range(1, 26):
                  cipherWord = cipherUp(newWord, i)
                  print(cipherWord)
                  cHWord = hashlib.sha256(cipherWord.encode('utf-8'))
                  if(cHWord.hexdigest() == passHash):
                    print("***Password was cracked using sha256 hash algorithm with cipher***")
                    print("password: {}".format(cipherWord))
                    exit()
          else:
              hashedWord = hashlib.sha256(word.encode('utf-8'))
              #print("comparing: {} to {} ".format(hashedWord.hexdigest(), passHash))
              if(hashedWord.hexdigest() == passHash):
                print("***Password was cracked using sha256 hash algorithm***")
                print("password: {}".format(word))
                exit()

          word = fp.readline().strip('\n')
        fp.close()

#use sha512 to try to crack the password size of 128 characters
def sha512_hack_tool(passHash, CIPHER):
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')
        while word:
          if(CIPHER == "yes"):
              newWord = word
              for i in range(26):
                  cipherWord = cipherUp(newWord, i)
                  print(cipherWord)

                  cHWord = hashlib.sha512(cipherWord.encode('utf-8'))
                  print("comparing: {} to {}".format(cHWord.hexdigest(), passHash))
                  if(cHWord.hexdigest() == passHash):
                    print("***Password was cracked using sha512 hash algorithm with cipher***")
                    print("password: {}".format(cipherWord))
                    exit()
              #exit()
          else:
             hashedWord = hashlib.sha512(word.encode('utf-8'))
             #print("comparing: {} to {} ".format(hashedWord.hexdigest(), passHash))
             if(hashedWord.hexdigest() == passHash):
               print("***Password was cracked using sha512 hash algorithm***")
               print("password: {}".format(word))
               exit()
             #print("{}".format(hashedWord.hexdigest()))
          word = fp.readline().strip('\n')

        fp.close()


#use blake2b to try to crack the password size of 128 characters
def blake2b_hack_tool(passHash, CIPHER):
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')
        while word:
          if(CIPHER == "yes"):
              newWord = word
              for i in range(26):
                  cipherWord = cipherUp(newWord, i)
                  print(cipherWord)
                  cHWord = hashlib.blake2b(cipherWord.encode('utf-8'))
                  print("comparing: {} to {}".format(cHWord.hexdigest(), passHash))
                  if(cHWord.hexdigest() == passHash):
                    print("***Password was cracked using blake2b hash algorithm with cipher***")
                    print("password: {}".format(cipherWord))
                    exit()
              #exit()
          else:
             hashedWord = hashlib.blake2b(word.encode('utf-8'))
             #print("comparing: {} to {} ".format(hashedWord.hexdigest(), passHash))
             if(hashedWord.hexdigest() == passHash):
               print("***Password was cracked using blake2b hash algorithm***")
               print("password: {}".format(word))
               exit()
             #print("{}".format(hashedWord.hexdigest()))
          word = fp.readline().strip('\n')

        fp.close()





# print('Guaranteed:\n{}\n'.format(
#     ', '.join(sorted(hashlib.algorithms_guaranteed))))
#
# print('Available:\n{}'.format(
#     ', '.join(sorted(hashlib.algorithms_available))))
# a = "a52821b2db64438d547c73a7a7d57777"
# print(len(a))
i = "sin dios"
w = hashlib.blake2b(i.encode('utf-8'))
# z = hashlib.blake2s(i.encode('utf-8'))
# t = hashlib.sha1(i.encode('utf-8'))
# u = hashlib.sha224(i.encode('utf-8'))
# b = hashlib.sha256(i.encode('utf-8'))
# c = hashlib.sha384(i.encode('utf-8'))
# d = hashlib.sha3_224(i.encode('utf-8'))
# e = hashlib.sha3_256(i.encode('utf-8'))
# f = hashlib.sha3_384(i.encode('utf-8'))
g = hashlib.sha3_512(i.encode('utf-8'))
h = hashlib.sha512(i.encode('utf-8'))
# j = hashlib.shake_128(i.encode('utf-8'))
# k = hashlib.shake_256(i.encode('utf-8'))
#
#
#print(w.hexdigest())
print(len(w.hexdigest()))
# print(len(z.hexdigest()))
# print(len(t.hexdigest()))
# print(len(u.hexdigest()))
# print(len(b.hexdigest()))
# print(len(c.hexdigest()))
# print(len(d.hexdigest()))
# print(len(e.hexdigest()))
# print(len(f.hexdigest()))
print(len(g.hexdigest()))
print(len(h.hexdigest()))
# print(len(j.hexdigest()))
# print(len(k.hexdigest()))
# word = "sinDios"
# print(type(word))
# combinations = list(itertools.product([str(0),str(1),str(2),str(3),str(4),str(5),str(6),str(7),str(8), str(9)], repeat=5))
# string_list = map(''.join, combinations)
# for s in string_list:
#     print(word+s)
#     word = word + s
#     print(word)
#     exit()





#get the hash to crack
passHash= input("Input the hash of the password to crack: ")

#get the length of the hash
print("{} has a length of {}".format(passHash, len(passHash)))
if( len(passHash) == 32):
    md5_hack_tool(passHash, "no")
    md5_hack_tool(passHash, "yes")

elif( len(passHash) == 40):
    sha1_hack_tool(passHash, "no")
    sha1_hack_tool(passHash, "yes")

elif( len(passHash) == 64):
    blake2s_hack_tool(passHash, "no", "no")
    sha256_hack_tool(passHash, "no", "no")
    blake2s_hack_tool(passHash, "no", "yes")
    sha256_hack_tool(passHash, "no", "yes")
    blake2s_hack_tool(passHash, "yes", "no")
    sha256_hack_tool(passHash, "yes", "no")

elif( len(passHash) == 128):
    sha512_hack_tool(passHash, "no")
    sha512_hack_tool(passHash, "yes")
    blake2b_hack_tool(passHash, "no")
    blake2b_hack_tool(passHash, "yes")
