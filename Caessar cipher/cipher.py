from alphabets_logo import alphabet
def cipher(start_text,shift_by,cipher_direction):
  end_text=""
  shift_modified = shift_by%26
  if cipher_direction=='decode':
    shift_modified *= -1
  for char in start_text:
    if char in alphabet:
      position= alphabet.index(char)
      new_position=position+shift_modified
      end_text += alphabet[new_position]
      
    else:
      end_text += char
  print(f"{cipher_direction}d code is {end_text}")
  