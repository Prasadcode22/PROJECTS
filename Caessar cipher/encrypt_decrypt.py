from alphabets import alphabet

def encrypt(code_text, shift_by):
  caesar_cipher_text=""
  for letter in code_text:
    position = alphabet.index(letter)
    new_position=position+shift_by
    new_letter=alphabet[new_position]
    caesar_cipher_text  += new_letter
  print(caesar_cipher_text)
  
def decrypt(caesar_cipher_text, shift_by):
  secret_message=""
  for letter in caesar_cipher_text:
    position = alphabet.index(letter)
    new_position=position-shift_by
    secret_message +=alphabet[new_position]
  print(secret_message)
  