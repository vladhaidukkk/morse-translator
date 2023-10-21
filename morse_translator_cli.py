import argparse
from morse_translator import MorseTranslator


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help="text to be encoded or Morse code to be decoded")
    parser.add_argument(
        "-e",
        "--encode",
        action="store_true",
        help="encode a text to Morse code (has priority over decoding)"
    )
    parser.add_argument(
        "-d",
        "--decode",
        action="store_true",
        help="decode a Morse code to text"
    )
    parser.add_argument(
        "--dot",
        default=".",
        help="character used for dot (default: '.')",
        metavar=""
    )
    parser.add_argument(
        "--dash",
        default="-",
        help="character used for dash (default: '-')",
        metavar=""
    )
    parser.add_argument(
        "--separator",
        default=" ",
        help="character used for separator (default: ' ')",
        metavar=""
    )
    parser.add_argument(
        "--space",
        default="/",
        help="character used for space (default: '/')",
        metavar=""
    )
    return parser


def process_args(args):
    translator = MorseTranslator(dot=args.dot, dash=args.dash, separator=args.separator, space=args.space)
    if args.encode:
        return translator.encode(args.string)
    if args.decode:
        return translator.decode(args.string)
    raise ValueError("--encode or --decode is required")


def main():
    parser = create_parser()
    args = parser.parse_args()
    try:
        output = process_args(args)
        print(output)
    except ValueError as err:
        parser.error(str(err))


if __name__ == "__main__":
    main()
