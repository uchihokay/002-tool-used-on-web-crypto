import codecs

a = bytes.fromhex(input("var 1 = "))
b = bytes.fromhex(input("var 2 = "))

key = bytes(x^y for x,y in zip(a,b))

#translate byte to text
key_text = key.decode("utf-8")

print(key_text)
