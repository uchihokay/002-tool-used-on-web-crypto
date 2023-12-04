import codecs

a = bytes.fromhex(input())
text = a.decode("utf-8")

print(text)