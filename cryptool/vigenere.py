import string

alphabet = string.ascii_uppercase


def vigenere(text: str, keyword: str, decrypt: bool = False) -> str:
    text = text.upper()
    keyword = keyword.upper()
    N = len(alphabet)

    result = []
    key_index = 0

    for char in text:
        if char in alphabet:
            shift = alphabet.index(keyword[key_index % len(keyword)])
            if decrypt:
                shift = -shift

            alph_idx = alphabet.index(char)
            result.append(alphabet[(alph_idx + shift) % N])
            key_index += 1
        else:
            result.append(char)

    return "".join(result)
