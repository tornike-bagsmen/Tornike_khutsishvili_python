def main():
    encryption_deciphered = input("for deciphered press d another situation press e: ").lower()
    encryption = input("write:")

    decode_0 = "qwertyuiopq"
    decode_1 = "asdfghjkla"
    decode_2 = "zxcvbnmz"

    decode = decode_0 + decode_1 + decode_2
    print(decode)
    if encryption_deciphered == "e":
        
        for i in encryption:
            index = decode.index(f"{i}")
            index += 1
            print(decode[index], end = "")
    
    else:
        for i in encryption:
            index = decode.index(f"{i}")
            negative_index = encryption.index(i) - len(encryption)+1
            print(decode[negative_index], end = "")
            index -= 1
          
main()