from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
from lib import RSA, aes_gcm


def get_encryption_key_and_salt_from_rsa_message(message, block_size):
    message_bytes = message.to_bytes(
        block_size, 'big')

    encryption_key_and_salt = SHA256.new(message_bytes).digest().hex()

    encryption_key = encryption_key_and_salt[:block_size // 2]
    salt = encryption_key_and_salt[block_size // 2:]

    return (encryption_key, salt)


def encrypt(public_key, modulus, message):
    block_size = modulus.bit_length() // 4

    numbered_encryption_key_and_salt = int.from_bytes(
        get_random_bytes(block_size * 2), 'big') % modulus

    encryption_key, salt = get_encryption_key_and_salt_from_rsa_message(
        numbered_encryption_key_and_salt, block_size)

    cipher_text = aes_gcm.encrypt(encryption_key, message, salt)

    rsa_encrypted_key = RSA.encrypt(
        public_key, numbered_encryption_key_and_salt, modulus)

    hexed_rsa_encrypted_key = str(
        hex(rsa_encrypted_key)).rjust(block_size * 2, "0")

    return hexed_rsa_encrypted_key + cipher_text


def decrypt(secret_key, modulus, cipher_text):
    block_size = modulus.bit_length() // 4
    padded_hexed_key = cipher_text[:block_size * 2]

    hex_start = padded_hexed_key.find('0x')
    hexed_key = padded_hexed_key[hex_start:]

    rsa_encrypted_key = int(hexed_key, 16)

    rsa_decrypted_key = RSA.decrypt(secret_key, rsa_encrypted_key, modulus)

    encryption_key, salt = get_encryption_key_and_salt_from_rsa_message(
        int(rsa_decrypted_key), block_size)

    encrypted_text = cipher_text[block_size * 2:]

    decrypted_text = aes_gcm.decrypt(encryption_key, encrypted_text, salt)

    return decrypted_text
