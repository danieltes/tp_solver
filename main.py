#!/usr/bin/env python


import constants
import scanner
import parser 
import render
import codegen 


if __name__ == "__main__":
    """ Entrada principal. """

    try:
        input = raw_input
    except:
        pass

    input_str = input("entrada> ")
    scan = scanner.Scanner(input_str)
    '''
    token_type, token_value = scan.get_token()
    while token_type != constants.TOKEN_EOF:
        print("token: {0}, value: {1}".format(token_type, token_value))
        token_type, token_value = scan.get_token()
    '''
    parser = parser.ExpParser(scan)
    tree = parser.parse()
    render.render_tree(tree)
    codegen.gen(tree)

    import draw
    draw.draw()

