import math


def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def frombits(bits):
    chars = []

    for b in range((len(bits) // 8)):
        byte = bits[b * 8:(b + 1) * 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]


def main():
    with open("open_key_n.txt", "r", encoding="utf-8") as inp:
        n = int(inp.readline())
    with open("open_key_e.txt", "r", encoding="utf-8") as inp:
        e = int(inp.readline())
    with open("secret_key_d.txt", "r", encoding="utf-8") as inp:
        d = int(inp.readline())

    with open("open_text.txt", "r", encoding="utf-8") as inp:
        open_text = inp.read().strip()

    open_text_bits = tobits(open_text)
    max_block_len = int(math.log(n, 2))
    max_block_len -= max_block_len % 8
    print("Maximum block length:", max_block_len)
    open_text_bits_length = len(open_text_bits)
    print("Len (in bits) of open text", open_text_bits_length)

    # Encryption
    with open("encrypted_text.txt", "w+", encoding="utf-8") as encrypted_file:
        for i in range(math.ceil(open_text_bits_length / max_block_len)):
            chunk = open_text_bits[i * max_block_len: min((i + 1) * max_block_len, open_text_bits_length)]
            chunk_number = 0
            for i in range(0, len(chunk)):
                chunk_number += chunk[i] * (2 ** (len(chunk) - 1 - i))
            hidden_msg = pow(chunk_number, e, n)
            encrypted_file.write(f"{hidden_msg}\n")

    # Decryption
    with open("encrypted_text.txt", "r", encoding="utf-8") as encrypted_file, \
            open("decrypted_file.txt", "w+", encoding="utf-8") as decrypted_file:
        for line in encrypted_file:
            hidden_msg = int(line)
            decrypted_msg = pow(hidden_msg, d, n)
            decrypted_list_of_bits = bitfield(decrypted_msg)
            for i in range(8 - len(decrypted_list_of_bits) % 8):
                decrypted_list_of_bits.insert(0, 0)
            decrypted_msg = frombits(decrypted_list_of_bits)
            decrypted_file.write(f"{decrypted_msg}")


if __name__ == '__main__':
    main()
