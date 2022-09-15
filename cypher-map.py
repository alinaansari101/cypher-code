alphabet = {
  'a' : 'c',
  'b' : 'd',
  'c' : 'e',
  'd' : 'f',
  'e' : 'g',
  'f' : 'h',
  'g' : 'i',
  'h' : 'j',
  'i' : 'k',
  'j' : 'l',
  'k' : 'm',
  'l' : 'n',
  'm' : 'o',
  'n' : 'p',
  'o' : 'q',
  'p' : 'r',
  'q' : 's',
  'r' : 't',
  's' : 'u',
  't' : 'v',
  'u' : 'w',
  'v' : 'x',
  'w' : 'y',
  'x' : 'z',
  'y' : 'a', 
  'z' : 'b'
}

def encrypt(string):
  cypher = ""
  for char in string:
   cypher += alphabet[char]
  return cypher  
     
string = input("Word:")
key = int(input("Key:"))

enc_text = encrypt(string)
print(enc_text)


