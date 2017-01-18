def caesar(plaintext, offset):
    '''Returns ciphertext obtained by transforming every letter
    in the plaintext by a Caesar cipher by the specified shift.
    Non-letter characters should remain unchanged in the ciphertext.'''

    ciphertext = ""

    for ch in plaintext:
        # to shift lowercase letters
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = ord(ch) + offset
            ch = chr(ch)
            #to keep in the range of lowercase letters
            while ord(ch) > 122:
                ch = ord(ch) - 26
                ch = chr(ch)
        # to shift uppercase letters
        if ord(ch) >= 65 and ord(ch) <= 90:
            ch = ord(ch) + offset
            ch = chr(ch)
            #to keep in the range of uppercase letters
            while ord(ch) > 90:
                ch = ord(ch) - 26
                ch = chr(ch)
        # adds shifted character to empty string
        ciphertext += ch

    return ciphertext

def main():
    message = raw_input('Enter a message: ')
    shift = int(raw_input('Enter a non-negative integer: '))

    ciphertext = caesar(message, shift)
    print ciphertext

main()
