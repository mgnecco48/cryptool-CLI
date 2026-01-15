import argparse
from pathlib import Path
import sys

from cryptool.caesar import caesar
from cryptool.vigenere import vigenere


def read_input(text_arg: str | None, input_file: Path | None) -> str:
    if input_file:
        return input_file.read_text(encoding="utf-8")

    if text_arg:
        return text_arg

    if not sys.stdin.isatty():
        return sys.stdin.read()

    return input("Enter text -> ")


def handle_list(args):
    CYAN = "\033[96m"
    RESET = "\033[0m"

    print("Available ciphers:")
    print(f"  • {CYAN}caesar{RESET}     – Shift cipher (classical)")
    print(f"  • {CYAN}vigenere{RESET}   – Keyword-based polyalphabetic cipher")


def handle_caesar(args):
    text = (
        " ".join(args.text)
        if args.text
        else read_input(None, args.input)
    )

    if args.encrypt:
        result = caesar(text, args.key)
    else:
        result = caesar(text, -args.key)

    print(result)


def handle_vigenere(args):
    text = (
        " ".join(args.text)
        if args.text
        else read_input(None, args.input)
    )

    if not args.key.isalpha():
        print("Error: Vigenère key must contain letters only.", file=sys.stderr)
        sys.exit(1)

    result = vigenere(
        text,
        args.key,
        decrypt=args.decrypt
    )

    print(result)


def cli():
    parser = argparse.ArgumentParser(
        prog="cryptool",
        description=(
            "Simple encryption CLI tool, made by \033[95mMartin Gnecco\033[0m.\n"
            "Use `cryptool \033[96mlist\033[0m` to see available ciphers.\n"
            "Use `cryptool <cipher> \033[96m--help\033[0m` for cipher options."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    sub = parser.add_subparsers(dest="cipher", required=True)

    # ===== Caesar subcommand =====
    p_caesar = sub.add_parser("caesar", help="Caesar cipher")

    mode_caesar = p_caesar.add_mutually_exclusive_group(required=True)
    mode_caesar.add_argument(
        "-enc", "--encrypt", action="store_true", help="Encrypt")
    mode_caesar.add_argument(
        "-dec", "--decrypt", action="store_true", help="Decrypt")

    p_caesar.add_argument(
        "key",
        type=int,
        help="Shift key (integers only)"
    )

    p_caesar.add_argument(
        "text",
        nargs="*",
        help='Text to encrypt/decrypt (optional if using -i)'
    )

    p_caesar.add_argument(
        "-i", "--input",
        type=Path,
        help="Input file"
    )

    p_caesar.set_defaults(func=handle_caesar)

    # ===== Vigenère subcommand =====
    p_vig = sub.add_parser("vigenere", help="Vigenère cipher")

    mode_vig = p_vig.add_mutually_exclusive_group(required=True)
    mode_vig.add_argument("-enc", "--encrypt",
                          action="store_true", help="Encrypt")
    mode_vig.add_argument("-dec", "--decrypt",
                          action="store_true", help="Decrypt")

    p_vig.add_argument(
        "key",
        type=str,
        help="Keyword (letters only)"
    )

    p_vig.add_argument(
        "text",
        nargs="*",
        help="Text to encrypt/decrypt (optional if using -i)"
    )

    p_vig.add_argument(
        "-i", "--input",
        type=Path,
        help="Input file"
    )

    p_vig.set_defaults(func=handle_vigenere)

    # ===== list subcommand =====
    p_list = sub.add_parser("list", help="List available ciphers")
    p_list.set_defaults(func=handle_list)

    # ===== Parse & dispatch =====
    args = parser.parse_args()
    args.func(args)
