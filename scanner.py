#!/usr/bin/env python

import constants


class Scanner:
    """ Escaner basado en el propuesto por Louden en
        Contruccion de compiladores (2004 - Thomson) """
    def __init__(self, input_str):
        """ Ctor. """
        self.__input_str = input_str
        self.__char_index = 0

    def __get_next_char(self):
        """ Obtiene el siguiente caracter desde la entrada. """
        # Obtengo el siguiente caracter si puedo.
        if self.__char_index < len(self.__input_str):
            char_value = self.__input_str[self.__char_index]
            self.__char_index = self.__char_index + 1
            return char_value
        else:
            # Sumo una posicion mas aunque no haya podido leer
            # para poder usar __unget_next_char en el ultimo
            # caracter.
            self.__char_index = self.__char_index + 1
        return constants.EOF

    def __unget_next_char(self):
        """ Reajusta un caracter en la entrada volviendo a la posicion anterior. """
        self.__char_index = self.__char_index - 1

    def get_token(self):
        """ Obtiene el siguiente token. """
        current_token_type = constants.TOKEN_NONE
        current_token_value = constants.DEFAULT_TOKEN_VALUE
        state_type = constants.STATE_START
        while state_type != constants.STATE_DONE:
            save_char = True
            char_value = self.__get_next_char()
            if state_type == constants.STATE_START:
                if char_value.isdigit() is True:
                    state_type = constants.STATE_INNUMBER
                elif char_value == " ":
                    save_char = False
                else:
                    state_type = constants.STATE_DONE
                    if char_value == "+":
                        current_token_type = constants.TOKEN_PLUS
                    elif char_value == "-":
                        current_token_type = constants.TOKEN_MINUS
                    elif char_value == "*":
                        current_token_type = constants.TOKEN_TIMES
                    elif char_value == "/":
                        current_token_type = constants.TOKEN_OVER
                    elif char_value == "(":
                        current_token_type = constants.TOKEN_LPAREN
                    elif char_value == ")":
                        current_token_type = constants.TOKEN_RPAREN
                    elif char_value == "=":
                        current_token_type = constants.TOKEN_EQUAL
                    elif char_value == "x":
                        current_token_type = constants.TOKEN_X
                    elif char_value == "y":
                        current_token_type = constants.TOKEN_Y
                    elif char_value == "^":
                        current_token_type = constants.TOKEN_POWER
                    elif char_value == constants.EOF:
                        save_char = False
                        state_type = constants.STATE_DONE
                        current_token_type = constants.TOKEN_EOF
                    else:
                        current_token_type = constants.TOKEN_ERROR
            elif state_type == constants.STATE_INNUMBER:
                if char_value.isdigit() is False:
                    self.__unget_next_char()
                    save_char = False
                    state_type = constants.STATE_DONE
                    current_token_type = constants.TOKEN_NUMBER
            else:
                print "Error en el escaner. No deberia haber llegado hasta aca :("
                state_type = constants.STATE_DONE
                current_token_type = constants.TOKEN_ERROR

            if save_char is True:
                current_token_value += str(char_value)

        return [current_token_type, current_token_value]
