def login(senha1):
    from Cryptodome.Cipher import Blowfish
    from Cryptodome import Random
    from struct import pack

    BF = Blowfish.block_size
    Chave = b'Alohomora'
    CDS = Random.new().read(BF)
    cipher = Blowfish.new(Chave, Blowfish.MODE_CBC, CDS)
    plaintext = senha1
    plen = BF - divmod(len(plaintext),BF)[1]
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    msg = CDS + cipher.encrypt(plaintext + padding)
    print(repr(msg)) 

login(b'TopTop123@')