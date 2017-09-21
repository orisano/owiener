import os.path

from setuptools import setup

readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md")
try:
    from m2r import parse_from_file
    readme = parse_from_file(readme_file)
except ImportError:
    with open(readme_file) as f:
        readme = f.read()

setup(
    name="owiener",
    version="1.0.2",
    author="orisano",
    author_email="owan.orisano@gmail.com",
    description="A Python3 implementation of the Wiener attack on RSA",
    long_description=readme,
    license="MIT",
    url="https://github.com/orisano/owiener",
    py_modules=["owiener"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Security :: Cryptography",
    ],
)
