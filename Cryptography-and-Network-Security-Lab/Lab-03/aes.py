from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# Take message from user
message = input("Enter the message: ").encode()


# Generate random 16-byte key
key = get_random_bytes(16)

# Generate random 16-byte IV
iv = get_random_bytes(16)


# Encryption
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(message, AES.block_size))


print("\n----- AES ENCRYPTION -----")
print("Original Message :", message.decode())
print("Key              :", key.hex())
print("IV               :", iv.hex())
print("Encrypted        :", ciphertext.hex())


# Decryption
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)


print("\n----- AES DECRYPTION -----")
print("Decrypted Message:", decrypted.decode())