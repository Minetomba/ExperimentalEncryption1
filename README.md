---

# baseULTRA

`baseULTRA` is a custom encoder/decoder script built in Python that performs:

- Base-N string encoding using printable characters.
- Optional obfuscation via deterministic character index swapping (stored as reversible mixes).
- Compact serialization using base85 and base16.
- Reversible transformation with strict data integrity.

This script is ideal for obfuscation, encoding with custom bases, or embedding compact, reversible secrets in various formats.

---

## ⚙️ Features

- ✅ Base-N (e.g., base 10000) encoding using printable characters
- 🔀 Obfuscation via randomized reversible character swaps
- 💾 Mix files (for reversible shuffling)
- 🧼 Clean decoding with strict validation
- 📦 Compact: All in a single Python file

---

## 🔧 Usage

### Encode

```bash
python baseULTRA.py encode "<your-text>" <base> --save-mixes-file mixes.txt
````

**Arguments:**

* `encode` — operation mode
* `<your-text>` — string to encode
* `<base>` — numerical base (e.g., `10000`)
* `--save-mixes-file` — (optional) file to save the generated character swaps

**Example:**

```bash
python baseULTRA.py encode "Hello World" 10000 --save-mixes-file mixes.txt
```

**Output:**

```
Obfuscated base16-encoded string (example):
E281A3E28...
```

---

### Decode

```bash
python baseULTRA.py decode "<encoded-text>" <base> --mixes-file mixes.txt
```

**Arguments:**

* `decode` — operation mode
* `<encoded-text>` — base16 string to decode
* `<base>` — same base used during encoding
* `--mixes-file` — required file with saved swaps from encoding step

**Example:**

```bash
python baseULTRA.py decode "E281A3E28..." 10000 --mixes-file mixes.txt
```

**Output:**

```
Hello World
```

---

## 🧠 Internals

* **Encoding**

  * Converts input to an integer (`base 256`)
  * Converts integer to `base-N` using printable characters (offset by +50)
  * Joins encoded characters with Unicode U+2063 as delimiter
  * Applies 500–1000 random index swaps to obfuscate further

* **Mix File**

  * Stores the swaps as a JSON-encoded, base85-compressed structure
  * Required for deterministic decoding

* **Decoding**

  * Reverse base16
  * Reverse swaps
  * Convert from base-N back to original string

---

## 🔐 Design Notes

* Mixes ensure **data isn’t recoverable** without the `--mixes-file`
* Uses `\u2063` (Invisible Separator) to delimit encoded characters
* Script is **fully deterministic** if the mix file is preserved
* Not cryptographically secure — obfuscation only

---

## 📁 File List

* `baseULTRA.py` — main script
* `mixes.txt` — generated mix file (on encoding with `--save-mixes-file`)

---

## 🚨 Disclaimer

This tool is **not a cryptographic algorithm** and should **not** be used for sensitive data protection. It is meant for educational, experimental, or light obfuscation purposes only.

---
