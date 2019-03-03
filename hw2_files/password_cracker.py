import hashlib
import itertools
import string
import collections

'''---------------------Programmer notes-------------------------------'''
#encode() converts the string into bytes to be accepted by hash function
#digest() returns the encoded data in byte format
#hexdigest() returns the encoded dat n hexadecimal format
'''--------------------------------------------------------------------'''

# fuunction used to transform a word with a caesar cipher key
def cipherUp(orginalString, key):
    #create queue of lower case alphabet
    lowerCaseAlphabetList = collections.deque(string.ascii_lowercase)
    #now rotate the queue with provided key
    lowerCaseAlphabetList.rotate(key)
    #create a string with no spaces between of the rotated alphabet
    alphabetString = ''.join(list(lowerCaseAlphabetList))
    #replace all characters with created rotaed alphabet string
    cipherString = orginalString.translate(str.maketrans(string.ascii_lowercase, alphabetString))
    return cipherString

#function used to crack userName7 password -- substitution cipher
def sub_hack_tool(dictString):
    #cipher alphabet mapping
    alphaKey = "sgquntivdaejrozhpyfclwxmkb"
    #return string that has replace all plain text with cipher alphabet mapping
    return dictString.translate(str.maketrans(string.ascii_lowercase, alphaKey))


#use md5 to try to crack the password size of 32 characters
def md5_hack_tool(passHash, SALT, SUB):
    orgWord = ""
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')
        while word:
          if(SALT == "yes"):
              word = word + "SALT"
          if(SUB == "yes"):
              orgWord = word
              word = sub_hack_tool(word)
          hashedWord = hashlib.md5(word.encode('utf-8'))
          if(hashedWord.hexdigest() == passHash):
              if(SUB == "yes"):
                  print("***Password was cracked using md5 hash algorithm***")
                  print("password: {}".format(orgWord))
                  exit()
              print("***Password was cracked using md5 hash algorithm***")
              print("password: {}".format(word))
              exit()
          word = fp.readline().strip('\n')
        fp.close()

#use sha1 to try to crack the password size of 40 characters -- used for leet speak only
def sha1_hack_tool(passHash, SALT):
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')
        while word:
            #replace characters for leet speak before hashing word
            word = word.replace('a', '4')
            word = word.replace('c', '(')
            word = word.replace('e', '3')
            word = word.replace('l', '1')
            word = word.replace('o', '0')
            word = word.replace('s', '5')
            hashedWord = hashlib.sha1(word.encode('utf-8'))
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
               #create a list of all the combinations
               combinations = list(itertools.product([str(0),str(1),str(2),str(3),str(4),str(5),str(6),str(7),str(8), str(9)], repeat=5))
               #create a string of all combinations with no spaces
               string_list = map(''.join, combinations)
               #iterate through all combinations for each word in the dictionary
               for s in string_list:
                   cWord = word + s
                   hWord = hashlib.blake2s(cWord.encode('utf-8'))
                   if(hWord.hexdigest() == passHash):
                     print("***Password was cracked using blake2s hash algorithm with SALT***")
                     print("password: {}".format(word))
                     exit()
            elif(CIPHER == "yes"):
                #save the orginal word
                newWord = word
                #iterate throught all possible shift keys
                for i in range(1, 26):
                    #cipherUp returns string with new key shift
                    cipherWord = cipherUp(newWord, i)
                    cHWord = hashlib.blake2s(cipherWord.encode('utf-8'))
                    if(cHWord.hexdigest() == passHash):
                      print("***Password was cracked using blake2s hash algorithm with cipher***")
                      print("password: {}".format(cipherWord))
                      exit()
            else:
              hashedWord = hashlib.blake2s(word.encode('utf-8'))
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
                #create a list of all the combinations
                combinations = list(itertools.product([str(0),str(1),str(2),str(3),str(4),str(5),str(6),str(7),str(8), str(9)], repeat=5))
                #create a string of all combinations with no spaces
                string_list = map(''.join, combinations)
                #iterate through all combinations for each word in the dictionary
                for s in string_list:
                    cWord = word + s
                    hWord = hashlib.sha256(cWord.encode('utf-8'))
                    if(hWord.hexdigest() == passHash):
                      print("***Password was cracked using sha256 hash algorithm with SALT***")
                      print("password: {}".format(word))
                      exit()

            elif(CIPHER == "yes"):
                #save the orginal word
                newWord = word
                #iterate throught all possible shift keys
                for i in range(1, 26):
                    #cipherUp returns string with new key shift
                    cipherWord = cipherUp(newWord, i)
                    cHWord = hashlib.sha256(cipherWord.encode('utf-8'))
                    if(cHWord.hexdigest() == passHash):
                      print("***Password was cracked using sha256 hash algorithm with cipher***")
                      print("password: {}".format(cipherWord))
                      exit()
            else:
                hashedWord = hashlib.sha256(word.encode('utf-8'))
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
                #iterate throught all possible shift keys
                for i in range(26):
                    #cipherUp returns string with new key shift
                    cipherWord = cipherUp(newWord, i)
                    cHWord = hashlib.sha512(cipherWord.encode('utf-8'))
                    if(cHWord.hexdigest() == passHash):
                      print("***Password was cracked using sha512 hash algorithm with cipher***")
                      print("password: {}".format(word))
                      exit()
            else:
               hashedWord = hashlib.sha512(word.encode('utf-8'))
               if(hashedWord.hexdigest() == passHash):
                 print("***Password was cracked using sha512 hash algorithm***")
                 print("password: {}".format(word))
                 exit()
            word = fp.readline().strip('\n')
        fp.close()


#use blake2b to try to crack the password size of 128 characters
def blake2b_hack_tool(passHash, CIPHER):
    with open('dictionary.txt') as fp:
        word = fp.readline().strip('\n')
        while word:
            hjhlhl
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
            else:
               hashedWord = hashlib.blake2b(word.encode('utf-8'))
               if(hashedWord.hexdigest() == passHash):
                 print("***Password was cracked using blake2b hash algorithm***")
                 print("password: {}".format(word))
                 exit()
            word = fp.readline().strip('\n')
        fp.close()











#get the hash to crack
passHash= input("Input the hash of the password to crack: ")

#crack the password according to the len of the hash string
if( len(passHash) == 32):
    md5_hack_tool(passHash, "no", "no")
    md5_hack_tool(passHash, "yes", "no")
    md5_hack_tool(passHash, "no", "yes")

elif( len(passHash) == 40):
    sha1_hack_tool(passHash, "no")
    sha1_hack_tool(passHash, "yes")

elif( len(passHash) == 64):
    sha256_hack_tool(passHash, "no", "no")
    blake2s_hack_tool(passHash, "no", "no")
    sha256_hack_tool(passHash, "no", "yes")
    blake2s_hack_tool(passHash, "no", "yes")
    sha256_hack_tool(passHash, "yes", "no")
    blake2s_hack_tool(passHash, "yes", "no")

elif( len(passHash) == 128):
    sha512_hack_tool(passHash, "no")
    sha512_hack_tool(passHash, "yes")
    blake2b_hack_tool(passHash, "no")
    blake2b_hack_tool(passHash, "yes")
