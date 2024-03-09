# caesarASCII

A python caesar encode and decode only in ascii, and keeps punctuation.

Made this up because i didn't find simpler and more straight to the point tool

## Usage

> Note: if decode doesn't work, try with encode and with the same key

```python
key = 20
plaintext = 'supersecret'

encoded = caesarEncode(plaintext, key)
print(encoded)

#output : yavkxykixkz
```
```python
key = 20
encoded = 'yavkxykixkz'

decoded = caesarDecode(encoded, key)
print(decoded)

#output : supersecret
```

