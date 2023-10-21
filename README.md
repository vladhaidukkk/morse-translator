# Morse Translator CLI

The Morse Translator CLI is a simple command-line tool designed to help you easily encode and decode Morse code messages. Whether you need to send or receive Morse code, this tool makes the process straightforward and efficient.

## Installation

To install the Morse Translator CLI, you will need to have Python and pip installed on your system. Run this command:

```bash
pip install -i https://test.pypi.org/simple/ morse-translator
```

_It is important to note that this package is published on TestPyPI._

## Usage

The Morse Translator CLI provides two main options: `--encode` and `--decode`.

To encode a text message into Morse code, use the following command:
```bash
morse_translator --encode "Text message here"
```

To decode a Morse code into readable text, use the following command:
```bash
morse_translator --decode "Morse code here"
```

To see all options, use the following command:
```bash
morse_translator --help
```

## Examples

### Encoding a Text Message

```bash
$ morse_translator --encode "Hello, World!"
.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.-- 
```

### Decoding Morse Code

```bash
$ morse_translator --decode ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"
HELLO, WORLD!
```
