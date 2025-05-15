from pydoover.docker import run_app

from .app_config import SampleConfig
from .application import SampleApplication

def run():
    """
    Run the application.
    """
    run_app(SampleApplication(config=SampleConfig()))

if __name__ == "__main__":
    run()
