import string
from sys import stderr

CONST_STRINGS = ["9DOLLAR0", "Cheby", "Homework"]


def main():
    lower_case_letters = string.ascii_lowercase
    lower_case_dict = {letter: i for i, letter in enumerate(lower_case_letters)}
    upper_case_letters = string.ascii_uppercase
    upper_case_dict = {letter: i for i, letter in enumerate(upper_case_letters)}
    digits = string.digits
    digits_dict = {digit: i for i, digit in enumerate(digits)}
    alphabet_length = len(lower_case_letters)
    word_1 = CONST_STRINGS[0]
    word_2 = CONST_STRINGS[1]
    word_3 = CONST_STRINGS[2]

    result = ""
    # Step 1
    sym = word_1[0]
    if sym in lower_case_letters:
        next_letter_id = (lower_case_dict[sym] + 1) % alphabet_length
        result += lower_case_letters[next_letter_id] + lower_case_letters[next_letter_id + 1]
    elif sym in upper_case_letters:
        next_letter_id = (upper_case_dict[sym] + 1) % alphabet_length
        result += upper_case_letters[next_letter_id] +upper_case_letters[next_letter_id + 1]
    else:
        next_digit_id = (digits_dict[sym] + 1) % 10
        result += digits[next_digit_id] + digits[next_digit_id + 1]
        pass
    # Step 2
    sym = word_2[2]
    if sym in lower_case_letters:
        next_letter_id = (lower_case_dict[sym] - 1) % alphabet_length
        result += lower_case_letters[next_letter_id]
    elif sym in upper_case_letters:
        next_letter_id = (upper_case_dict[sym] - 1) % alphabet_length
        result += upper_case_letters[next_letter_id]
    else:
        next_digit_id = (digits_dict[sym] + 1) % 10
        result += digits[next_digit_id]
    # Step 3
    if len(word_3) % 2 == 1:
        sym = word_3[3]
        offset = 1
    else:
        sym = word_3[len(word_3) //2  - 1]
        offset = -1

    if sym in lower_case_letters:
        next_letter_id = (lower_case_dict[sym] + offset) % alphabet_length
        result += lower_case_letters[next_letter_id]
    elif sym in upper_case_letters:
        next_letter_id = (upper_case_dict[sym] + offset) % alphabet_length
        result += upper_case_letters[next_letter_id]
    else:
        next_digit_id = (digits_dict[sym] + 1) % 10
        result += digits[next_digit_id]

    # Step 4
    letter_id = len(word_1) + len(word_2) - 1
    result += lower_case_letters[letter_id % alphabet_length]
    print("Calculated password:",result)
    from getpass import getpass
    password = getpass()
    stderr.write("*" * len(password) + "\n")
    print(f"Check: user typed password\"{password}\"")
    if password == result:
        print("True password")
    else:
        print("Invalid password")


if __name__ == '__main__':
    main()
