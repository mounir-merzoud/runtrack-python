def caesarize_letter(letter, shift):
    if 'A' <= letter.upper() <= 'Z':
        start = ord('a') if letter.islower() else ord('A')
        return chr((ord(letter) - start + shift) % 26 + start)
    else:
        return letter

def caesarize(text, shift):
    return ''.join([caesarize_letter(letter, shift) for letter in text])

def uncaesarize(text, shift):
    return ''.join([caesarize_letter(letter, -shift) for letter in text])

message_original = 'Hello World'
decalage = 3
message_chiffre = caesarize(message_original, decalage)
message_dechiffre = uncaesarize(message_chiffre, decalage)

print("Message original:", message_original)
print("Message chiffré:", message_chiffre)
