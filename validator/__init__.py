VERSION = (0, 2, 0)


def get_version():
    return '.'.join(map(str, VERSION))


__version__ = get_version()
