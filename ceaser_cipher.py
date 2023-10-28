def caesar_cipher(input_string):
    input_lines = input_string.strip().split()
    n = int(input_lines[0])
    messages = list(map(int if type(i)==int else str, input_lines[1:]))
    
    output = []
    for i in range(n):
        shift = messages[i*2]
        message = messages[i*2 + 1]
        if 'the' in message:
            output.append(encrypt(message, shift))
        else:
            # message is ciphertext, so decrypt it
            output.append(decrypt(message, shift))
    return output

def encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            plaintext += char
    return plaintext


