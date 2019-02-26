import hashlib

#notes--
#encode() converts the string into bytes to be accepted by hash function
#digest() returns the encoded data in byte format
#hexdigest() returns the encoded dat n hexadecimal format

#use md5 to try to crack the password
def md5_hack_tool(passHash):
    with open('dictionary.txt') as fp:
        word = fp.readline()
        while word:
          print("{}".format(word))
          hashedWord = hashlib.md5(word.encode())
          if(passHash == hashedWord):
            print("Found a match: {} , hash: {}".format(word, hashedWord))
          #print("{}".format(hashedWord.hexdigest()))
          word = fp.readline()






#get the hash to crack
passHash= input("Input the hash of the password to crack: ")
print(passHash)
md5_hack_tool(passHash)
