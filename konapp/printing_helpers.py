_DEFAULT_SEPARATOR = '*'
_DEFAULT_LINE_LENGTH = 79


def print_surrounded(text: str, separator: str = '*', line_length: int = _DEFAULT_LINE_LENGTH):
    """ prints a text surrounded by two lines full of the separator char """

    print("{separator}\n{text}\n{separator}".format(separator=separator * line_length,
                                                    text=text))
