def senha(senha2):
    from Cryptodome.Cipher import Blowfish
    from struct import pack

    BF = Blowfish.block_size
    Chave = b'Alohomora'
    texto_encriptado = senha2
    CDS = texto_encriptado[:BF]
    texto_encriptado = texto_encriptado[BF:]

    cipher = Blowfish.new(Chave, Blowfish.MODE_CBC, CDS)
    msg = cipher.decrypt(texto_encriptado)

    last_byte = msg[-1]
    msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
    print(repr(msg))

senha(b'\xca\xc6\xd9\xb3\xd7I\x97\xdd+\x85\xe6\xbd\x1e\x92,\xfa&\x97<\xc2\x01r\xa9g')