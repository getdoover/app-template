import random

from pydoover.docker import Application, run_app
from pydoover.config import Schema


class SampleSimulator(Application):
    def main_loop(self):
        self.set_tag("random_value", random.randint(1, 100))


if __name__ == "__main__":
    run_app(SampleSimulator(config=Schema()))
