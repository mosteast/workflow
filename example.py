import fire
import os


class Example(object):
    """A simple example class."""

    def double(self, number):
        return 2 * number

    def list(self):
        os.system('ls')


if __name__ == '__main__':
    fire.Fire(Example)
