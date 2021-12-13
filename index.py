from lib import RSA_AES, RSA

size = 1024

N, e, d = RSA.init(size)

cipher_text = RSA_AES.encrypt(e, N, "Test")
decrypted_text = RSA_AES.decrypt(d, N, cipher_text)

print(decrypted_text)
