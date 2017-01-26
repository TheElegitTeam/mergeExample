def caesar(plaintext, offset):
    '''Returns ciphertext obtained by transforming every letter
    in the plaintext by a Caesar cipher by the specified shift.
    Non-letter characters should remain unchanged in the ciphertext.'''

    

    for ch in plaintext:
        # to shift uppercase letters


            ch = chr(ch)
            #to keep in the range of uppercase letters
            while ord(ch) > 90:


        # to shift lowercase letters
        if ord(ch) >= 97 and ord(ch) <= 122:

            ch = chr(ch)
            #to keep in the range of lowercase letters
            if ord(ch) > 122:



        # adds shifted character to empty string




    message = raw_input('Enter a message: ')


    ciphertext = caesar(message, shift)
    print ciphertext


