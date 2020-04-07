import random
import string


def main():
    alphabet = [x for x in string.ascii_uppercase]
    for x in string.digits:
        alphabet.append(x)
    V = 3
    passwd_length = int(input("Input password length\n"))
    passwd = ""
    for i in range(passwd_length):
        passwd += random.choice(alphabet)
    print("Your password:", passwd)
    num_combinations = len(alphabet) ** passwd_length
    t = num_combinations // V
    print(f"It would take no more than {t} minutes to crack your password", )


if __name__ == '__main__':
    main()
