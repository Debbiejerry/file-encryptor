from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Save the encryption key to a file
def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

# Load the encryption Key from a file
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

# Encrypt a file
def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as file:
            data = file.read()
            if not data:
                print(f"File '{input_file}' is empty.")
                return

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        with open(output_file, 'wb') as file:
            file.write(encrypted_data)

        print(f"File '{input_file}' encrypted to '{output_file}'")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

# Decrypt a file
def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as file:
            encrypted_data = file.read()
            if not encrypted_data:
                print(f"File '{input_file}' is empty.")
                return

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        with open(output_file, 'wb') as file:
            file.write(decrypted_data)

        print(f"File '{input_file}' decrypted to '{output_file}'")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

# Usage
if __name__ == "__main__":
    key_file = 'C:\\Users\\HP\\Desktop\\Cybersecurity\\encryption_key.key'
    key = load_key(key_file)

    input_file = 'C:\\Users\\HP\\Desktop\\Cybersecurity\\FileEncryptor\\plain_text.txt'
    encrypted_file = 'C:\\Users\\HP\\Desktop\\Cybersecurity\\FileEncryptor\\encrypted_file.txt'
    decrypted_file = 'C:\\Users\\HP\\Desktop\\Cybersecurity\\FileEncryptor\\decrypted_file.txt'

    encrypt_file(input_file, encrypted_file, key)
    decrypt_file(encrypted_file, decrypted_file, key)
