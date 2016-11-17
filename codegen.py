PY_OPS = {
    '^': '**',
}

def _write_term(n):
    if n.op is not None:
        els = ['({})'.format(_write_term(x)) for x in n.children]
        pyop = PY_OPS.get(n.op, n.op)
        return pyop.join(els)
    return n.value

def gen(tree):
    with open("compiled.py", "w") as fd:
        fd.write("exp = lambda x: {}".format(_write_term(tree)))
