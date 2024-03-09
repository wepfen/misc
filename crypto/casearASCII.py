lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesarDecode(ciphertext: str, key: int) -> str:

    decoded = '' 

    for char in ciphertext:
        if char in lowercase:
            letterPos = lowercase.index(char)
            decoded += lowercase[(letterPos+key)%26]
            
        elif char in uppercase:
            letterPos = uppercase.index(char)
            decoded += uppercase[(letterPos+key)%26]
            
        else:
            decoded += char

    return decoded 

def caesarEncode(plaintext: str, key: int) -> str:

    decoded = '' 

    for char in plaintext:
        if char in lowercase:
            letterPos = lowercase.index(char)
            decoded += lowercase[(letterPos-key)%26]
            
        elif char in uppercase:
            letterPos = uppercase.index(char)
            decoded += uppercase[(letterPos-key)%26]
            
        else:
            decoded += char

    return decoded 