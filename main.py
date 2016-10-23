#!/usr/bin/env python

import constants
import scanner


if __name__ == "__main__":
    """ Entrada principal. """
    input_str = raw_input("entrada> ")
    scan = scanner.Scanner(input_str)
    token_type, token_value = scan.get_token()
    while token_type != constants.TOKEN_EOF:
        print "token: {0}, value: {1}".format(token_type, token_value)
        token_type, token_value = scan.get_token()
