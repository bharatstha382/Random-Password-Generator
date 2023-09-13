#this project, Caesar cipher, is about creting encrypeted message. 
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
  def ceaser(text,shift_number):
    ciphre_text = ""
    for letter in text:
      if letter in alphabet:
        letter_index = alphabet.index(letter)
        if letter in alphabet:
          if direction == "encode":
            ciphre_index = letter_index + shift
            print(ciphre_index)
            ciphre_text+= alphabet[ciphre_index]
          # print(ciphre_index,ciphre_text)
          # print(letter_index) 
          else:
            ciphre_index = letter_index - shift
            ciphre_text+= alphabet[ciphre_index]
      else:
        ciphre_text += letter
    print(ciphre_text)
  ceaser(text,shift_number=shift)
  last_input = input("Type 'y if you want to repeat the procedure 'n' if you want to end\n").lower()
  if last_input != "y":
    should_continue = False
