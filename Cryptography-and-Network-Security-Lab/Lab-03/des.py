from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


# Take message from user
message = input("Enter the message: ").encode()

# Take DES key from user
key_input = input("Enter an 8-character key: ")

# Check key length
if len(key_input) != 8:
    print("Error: DES key must be exactly 8 characters.")
    exit()

key = key_input.encode()


# Generate IV
iv = b"12345678"


# ---------------- ENCRYPTION ----------------

cipher = DES.new(key, DES.MODE_CBC, iv)

padded_message = pad(message, DES.block_size)

ciphertext = cipher.encrypt(padded_message)


print("\n----- DES ENCRYPTION -----")
print("Original Message :", message.decode())
print("Key              :", key_input)
print("IV               :", iv.decode())
print("Encrypted        :", ciphertext.hex())


# ---------------- DECRYPTION ----------------

decipher = DES.new(key, DES.MODE_CBC, iv)

decrypted = unpad(
    decipher.decrypt(ciphertext),
    DES.block_size
)


print("\n----- DES DECRYPTION -----")
print("Decrypted Message:", decrypted.decode())