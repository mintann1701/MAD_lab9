def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # Shift each digit up by 3 numbers
        encoded_password += encoded_digit
    return encoded_password


def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print("Encoded password:", encoded_password)
        elif option == "2":
            decoded_password = decode(encoded_password)
            print("Your password has been decoded!")
            print("Decoded password:", decoded_password)
        elif option == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please enter a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
