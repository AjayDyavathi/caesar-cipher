class CaesarCipher():
    """ class that implements caesar cipher for files """

    def __init__(self, shift):
        self.modulo = 256
        self.shift = shift % self.modulo

    def encrypt(self, block):
        ciphertext = b""
        for byte in block:
            ciphertext += bytes([(byte + self.shift) % self.modulo])
        return ciphertext

    def decrypt(self, block):
        plaintext = b""
        for byte in block:
            plaintext += bytes([(byte - self.shift) % self.modulo])
        return plaintext
