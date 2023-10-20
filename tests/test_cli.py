import unittest
from parameterized import parameterized
from cli import create_parser, process_args


class TestCLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parser = create_parser()

    @parameterized.expand([
        (["--encode", "ABC"], "ABC", True, False, ".", "-", " ", "/"),
        (["--decode", ".- -... -.-."], ".- -... -.-.", False, True, ".", "-", " ", "/"),
        (
                ["--encode", "ABC", "--dot", "+", "--dash", "=", "--separator", "_", "--space", "&"],
                "ABC", True, False, "+", "=", "_", "&"
        ),
    ])
    def test_parser(self, input_args, string, encode, decode, dot, dash, separator, space):
        args = self.parser.parse_args(input_args)
        self.assertEqual(string, args.string)
        self.assertEqual(encode, args.encode)
        self.assertEqual(decode, args.decode)
        self.assertEqual(dot, args.dot)
        self.assertEqual(dash, args.dash)
        self.assertEqual(separator, args.separator)
        self.assertEqual(space, args.space)

    @parameterized.expand([
        (["--encode", "ABC"], ".- -... -.-."),
        (["--decode", ".- -... -.-."], "ABC"),
        (
                ["--encode", "ABC DE", "--dot", "+", "--dash", "=", "--separator", "_", "--space", "&"],
                "+=_=+++_=+=+_&_=++_+"
        ),
        (
                ["--decode", "+=_=+++_=+=+_&_=++_+", "--dot", "+", "--dash", "=", "--separator", "_", "--space", "&"],
                "ABC DE"
        ),
    ])
    def test_process_args(self, input_args, expected):
        args = self.parser.parse_args(input_args)
        output = process_args(args)
        self.assertEqual(expected, output)

    def test_process_args_exception(self):
        with self.assertRaises(ValueError):
            args = self.parser.parse_args(["ABC"])
            process_args(args)


if __name__ == "__main__":
    unittest.main()
