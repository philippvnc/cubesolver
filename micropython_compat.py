try:
    from micropython_compat import const
except ImportError:
    def const(x):
        return x