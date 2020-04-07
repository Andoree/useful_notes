import string


def code_text(text, table):
    result = ""
    for symbol in text:
        new_symbol = table.get(symbol)
        if new_symbol is not None:
            result += new_symbol
        else:
            result += symbol
    return result


def main():
    alphabet = [x for x in string.ascii_lowercase]
    print("Шифр моноалфавитной замены. Схема:")
    print("X_new = (a * X_old + m) mod |A|,\nгде A - алфавит.\n")
    inp = input("Введите a и m через пробел:\n")

    keys = inp.split()
    a = int(keys[0])
    m = int(keys[1])
    coding_table = {}
    decoding_table = {}
    for i, x_old in enumerate(alphabet):
        new_position = (i * a + m) % len(alphabet)
        x_new = alphabet[new_position]
        coding_table[x_old] = x_new
        decoding_table[x_new] = x_old
    while True:
        command = input("Введите команду (шифровать/дешифровать)\n")
        if command == "Выйти":
            break
        filename = input("Введите имя шифруемого/дешифруемого файла\n")
        if command == "шифровать":
            table = coding_table
        elif command == "дешифровать":
            table = decoding_table

        new_filename = code_text(filename, table)
        with open(filename, "r", encoding="utf-8") as inp, \
                open(new_filename, "w+", encoding="utf-8") as out:
            for old_line in inp:
                new_line = code_text(old_line, table)
                out.write(new_line)


if __name__ == '__main__':
    main()
