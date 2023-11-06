# file-encryptor
# File Encryption and Decryption Tool

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Introduction

The File Encryption and Decryption Tool is a Python script that allows you to encrypt and decrypt files using the Fernet symmetric encryption algorithm from the `cryptography` library. This tool provides a simple and secure way to protect sensitive data within files.

## Features

- Generate Encryption Key: Create a random encryption key.
- Save Encryption Key: Store the encryption key in a file for future use.
- Load Encryption Key: Load the encryption key from a file.
- Encrypt File: Encrypt the content of a file using the provided encryption key.
- Decrypt File: Decrypt an encrypted file using the encryption key.

## Getting Started

To get started with the File Encryption and Decryption Tool, follow these instructions:

### Prerequisites

- Python 3.x
- The `cryptography` library, which you can install using `pip install cryptography`.

### Usage

1. Generate an encryption key using the `generate_key()` function.
2. Save the encryption key to a file using the `save_key(key, key_file)` function.
3. Load the encryption key from a file using the `load_key(key_file)` function.

Example:
key = generate_key()
key_file = 'encryption_key.key'
save_key(key, key_file)
loaded key = load_key(key_file)

4. Encrypt a file using the encrypt_file(input_file, output_file, key) function, where input_file is the file you want to encrypt, output_file is the encrypted output file, and key is the encryption key.
Example:
encrypt_file('plain_text.txt', 'encrypted_file.txt', key)

5. Decrypt a file using the decrypt_file(input_file, output_file, key) function, where input_file is the encrypted file, output_file is the decrypted output file, and key is the encryption key.
Example:
decrypt_file('encrypted_file.txt', 'decrypted_file.txt', key)


## Contributing
Contributions to this project are welcome. To contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Test your changes.
5. Create a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License. You can find the full license text in the LICENSE file.
