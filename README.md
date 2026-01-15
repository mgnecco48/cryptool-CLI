# cryptool

```cryptool``` is a simple, educational command-line encryption tool written in Python.  
It implements classic ciphers with a clean, extensible CLI design and is intended as a learning project rather than a security tool.

The project focuses on:
- clear CLI structure
- readable, well-organized code
- practical use of `argparse` and Python packaging

---

## Features

- Caesar cipher (encrypt / decrypt)
- Vigenère cipher (encrypt / decrypt)
- File input or inline text input
- Piped input support
- Subcommand-based CLI (`cryptool caesar`, `cryptool vigenere`, `cryptool list`)

---

## Installation

Clone the repository and install in editable mode:

```pip install -e .```

*** Make sure to run the command from the outer cryptool directory

## Usage

**List available ciphers:**

```cryptool list```

**Caesar cipher**
Encrypt:

```cryptool caesar -enc 3 "HELLO WORLD"```

Decrypt:

```cryptool caesar -dec 3 "KHOOR ZRUOG"```

From a file:

```cryptool caesar -enc 3 -i message.txt```

**Vigenère cipher**
Encrypt:

```cryptool vigenere -enc KEY "HELLO WORLD"```

Decrypt:

```cryptool vigenere -dec KEY "RIJVS UYVJN"```

From a file:

```cryptool vigenere -enc SECRET -i message.txt```

**Help**

Top-level help:

```cryptool --help```

Cipher-specific help:

```cryptool caesar --help```
```cryptool vigenere --help```

---

**Disclaimer**
This tool is for educational purposes only.
It is not intended for real-world cryptographic security.

---

Author
Created by **Martin Gnecco**.
