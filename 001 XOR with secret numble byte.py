import codecs

var = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
for i in range(0,256) :
    flag = bytes(x ^ i for x in var)
    flag_hex = flag.hex()
    text = codecs.decode(flag_hex,'hex').decode('latin-1')
    print(text)
    
    
#XOR with a secret byte
#must try each byte from range 256