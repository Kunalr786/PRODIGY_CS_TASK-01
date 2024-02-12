def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += charENCR

    return result if mode == "encrypt" else caesar_cipher(result, -shift, "encrypt")


if __name__ == "__main__":
    print("Caesar Cipher")
    while True:
        mode = input("\nChoose mode (encrypt/decrypt): ").lower()
        if mode == "encrypt" or mode == "decrypt":
            break
        print("Invalid mode. Please choose either 'encrypt' or 'decrypt'.")

    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    output = caesar_cipher(message, shift, mode)

    if mode == "encrypt":
        print(f"Encrypted message: {output}")
    else:
        print(f"Decrypted message: {output}")