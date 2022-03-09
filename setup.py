import os
import sys
from shutil import rmtree

from setuptools import setup, Command


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package"
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.status("Building Source and Wheel (universal) distribution...")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")
        sys.exit()


setup(
    cmdclass={
        "upload": UploadCommand,
    },
)
