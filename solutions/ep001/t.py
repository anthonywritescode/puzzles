def somefunc(s: str) -> None:
    pass


x = 's'


somefunc('hi')  # ok
somefunc(x)  # error
somefunc(1)  # error
somefunc('hi', 1)  # error
