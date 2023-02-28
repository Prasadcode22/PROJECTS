# printing logo
from alphabets_logo import logo
print(logo)

from cipher import cipher

should_continue= True
while should_continue:
  purpose = input("Type 'encode' to encrypt or 'decode' to decrypt thr message!")
  message=input("Type your message:\n").lower()
  key=int(input("shift by:"))
  cipher(start_text=message,shift_by=key,cipher_direction=purpose)
  # wanna continue
  next_step=input("Type 'yes'if you want to continue it again. Otherwise type 'no'.\n")
  if next_step=='no':
    should_continue=False
    print("Goodbye, see you next time!")