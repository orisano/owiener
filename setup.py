from setuptools import setup

setup(
    name="owiener",
    version="1.0.0",
    author="orisano",
    author_email="owan.orisano@gmail.com",
    description="A Python3 implementation of the Wiener attack on RSA",
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
