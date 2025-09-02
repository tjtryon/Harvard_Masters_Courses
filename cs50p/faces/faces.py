""" faces.py
Author: TJ Tryon
Date: July 7, 2025

This program replaces emoticons with emojis. """


def convert(user_input):
    # Print user input, replace emoticons with emojis
    return user_input.replace(":)", "🙂").replace(":(", "🙁")


# Main will get user input, then call function convert() passing the string as a variable
def main():
    user_input = input("Enter your string with emoticons: ")
    user_input = convert(user_input)
    print(user_input)


# Calla main function
if __name__ == "__main__":
    main()
