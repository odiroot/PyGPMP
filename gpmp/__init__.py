from os.path import abspath, join, dirname

THIS_DIR = dirname(abspath(__file__))
ASSETS_DIR = join(THIS_DIR, "assets")


def get_asset(path):
    return join(ASSETS_DIR, path)
