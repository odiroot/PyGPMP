u"""Entry script for the whole GPMP application."""
import logging
import os

from gpmp.controllers import MainController


def setup_logger():
    if os.environ.get("DEBUG", False):
        # Only for development.
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(level=level)


def main():
    setup_logger()
    # Launch main application controller.
    controller = MainController()
    return controller.start()


if __name__ == "__main__":
    main()
