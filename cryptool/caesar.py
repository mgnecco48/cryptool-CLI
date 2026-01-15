import string

alphabet = string.ascii_uppercase


def caesar(text: str, key: int) -> str:
    text = text.upper()
    N = len(alphabet)
    key = key % N

    cyphertext = []

    for char in text:
        if char in alphabet:
            alph_idx = alphabet.index(char)
            cyphertext.append(alphabet[(alph_idx + key) % N])
        else:
            cyphertext.append(char)

    return "".join(cyphertext)
