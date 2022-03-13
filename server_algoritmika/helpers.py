def make_config(funcs: list)-> dict:
    conf = {}
    for fn in funcs:
        conf[fn.__name__] = fn
    return conf