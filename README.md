---

# baseULTRA

baseULTRA is a Python script to encode and decode strings using a custom Unicode base representation with reversible character swapping for obfuscation.

## Features

* Encode text into a custom base-N representation using printable characters
* Obfuscate encoded strings with random character swaps, storing swap information for decoding
* Decode obfuscated strings back to original text using saved swaps
* Compactly encode swaps using base85, and output strings in base16

## Usage

### Encoding

```bash
python baseULTRA.py encode your-text base [--save-mixes-file mixes.txt]
```

**Arguments:**

* encode : command to encode
* your-text : the string to encode (enclose in quotes if spaces exist)
* base : numeric base (integer >= 2)
* \--save-mixes-file : optional file path to save the swaps used during encoding

**Example:**

```bash
python baseULTRA.py encode Hello World 10000 --save-mixes-file mixes.txt
```

**Output:**
Prints an encoded and obfuscated base16 string. If --save-mixes-file is provided, the swaps are saved for decoding.

---

### Decoding

```bash
python baseULTRA.py decode encoded-text base [--mixes mixes] [--mixes-file mixes.txt]
```

**Arguments:**

* decode : command to decode
* encoded-text : the base16-encoded obfuscated string (enclose in quotes)
* base : the numeric base used during encoding
* \--mixes : optional base85-encoded JSON list of swaps
* \--mixes-file : optional file path to load swaps from (required if --mixes is not provided)

**Example:**

```bash
python baseULTRA.py decode E281A3D289E2... 10000 --mixes-file mixes.txt
```

**Output:**
Prints the original decoded string.

---

## Notes

* The swap information (mixes) is **required** to properly decode obfuscated strings.
* This tool provides reversible obfuscation, **not cryptographic security**.
* Internally, Unicode character U+2063 is used as a delimiter within encoded strings.

---
