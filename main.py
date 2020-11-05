#!/usr/bin/python3
# Usage: python3 main.py -e -s 7 source_file destination_file

import argparse
from caesar import CaesarCipher


def encrypt_file(source_file, dest_file, cipher):
    try:
        with open(source_file, "rb") as source:
            data = source.read()
            ciphertext = cipher.encrypt(data)
            with open(dest_file, "wb") as dest:
                dest.write(ciphertext)
                print("\033[92m\033[5mDONE\033[0m")

    except FileNotFoundError:
        print("\033[91mNo such file exists -\033[93m", source_file, "\033[0m")

    except Exception as e:
        print("\033[91m", str(e), "\033[0m")


def decrypt_file(source_file, dest_file, cipher):
    try:
        with open(source_file, "rb") as source:
            data = source.read()
            plaintext = cipher.decrypt(data)
            with open(dest_file, "wb") as dest:
                dest.write(plaintext)
                print("\033[92m\033[5mDONE\033[0m")

    except FileNotFoundError:
        print("\033[91mNo such file exists -\033[93m", source_file, "\033[0m")

    except Exception as e:
        print("\033[91m", str(e), "\033[0m")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encrypt", action="store_true")
    group.add_argument("-d", "--decrypt", action="store_true")
    parser.add_argument("-s", "--shift", type=int)
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    cipher = CaesarCipher(args.shift)
    if args.encrypt:
        encrypt_file(args.input_file, args.output_file, cipher)
    elif args.decrypt:
        decrypt_file(args.input_file, args.output_file, cipher)
    else:
        pass


if __name__ == "__main__":
    main()
