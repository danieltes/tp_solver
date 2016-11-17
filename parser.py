from constants import (TOKEN_EOF, TOKEN_LPAREN, TOKEN_RPAREN,
                       TOKEN_EQUAL, TOKEN_NUMBER, TOKEN_OVER,
                       TOKEN_POWER, TOKEN_PLUS, TOKEN_TIMES,
                       TOKEN_X, TOKEN_Y, TOKEN_MINUS)


class TreeNode:

    def __init__(self, parent=None):
        self.parent = parent
        self.children = []
        self.op = None
        self.value = None

    def add(self, n):
        n.parent = self
        self.children.append(n)


class ExpParser:

    def __init__(self, scanner):
        self._scanner = scanner
        self._token_type = None
        self._token = None

    def read_token(self):
        self._token_type, self._token = self._scanner.get_token()
        return self._token_type

    def parse(self):
        self.read_token()
        node = self._read_term()
        return node

    def _read_op(self):
        while self._token_type == TOKEN_RPAREN:
            self.read_token()
        op = self._token
        token = self.read_token()
        return op

    def _read_term(self):
        fn = self._read_factor()
        if self._token_type in (TOKEN_TIMES, TOKEN_OVER,
                                TOKEN_PLUS, TOKEN_MINUS,
                                TOKEN_POWER):
            op = self._read_op()
            node = TreeNode()
            node.op = op
            node.add(fn)
            node.add(self._read_factor())
            fn = node
        return fn

    def _read_factor(self):
        if self._token_type in (TOKEN_NUMBER, TOKEN_X, TOKEN_Y):
            node = TreeNode()
            node.value = self._token
            self.read_token()
        elif self._token_type is TOKEN_LPAREN:
            self.read_token()
            node = self._read_term()
            while self._token_type == TOKEN_RPAREN:
                self.read_token()
        else:
            node = None
        return node


