import io
import os
import sys
from shutil import rmtree

from setuptools import setup, Command

NAME = "owiener"
DESCRIPTION = "A Python3 implementation of the Wiener attack on RSA"
URL = "https://github.com:/orisano/owiener"
EMAIL = "owan.orisano@gmail.com"
AUTHOR = "orisano"
REQUIRES_PYTHON = ">=3.5.0"
VERSION = "1.0.4"

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


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
        try:
            self.status("Removing previous builds...")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution...")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine...")
        os.system("twine upload dist/*")

        self.status("Pushing git tags...")
        os.system("git tag v{0}".format(VERSION))
        os.system("git push --tags")

        sys.exit()


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=["owiener"],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security :: Cryptography",
    ],
    cmdclass={
        "upload": UploadCommand,
    },
)
