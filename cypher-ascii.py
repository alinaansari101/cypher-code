def encrypt(string, key):
  sentence = ""
  for char in string:
    num = ord(char)
    num += key
    sentence += chr(num)
  return sentence

def decrypt(string, key):
  sentence = ""
  for char in string:
    num = ord(char)
    num -= key
    sentence += chr(num) 
  return sentence  

string = input("Word:")
key = int(input("Key:"))
enc_text = encrypt(string, key)
print("your encrypted text is", enc_text)
print("your decrypted text is", decrypt(enc_text, key))
