# Melchi
from setuptools import setup, find_packages

setup(
    name="pyindependentreserve",
    version="0.4.1",
    description="Python client for Interacting with Independent Reserve API - The Bitcoin and Digital Currency Market",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MelchiSalins/pyindependentreserve",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="Bitcoin BlockChain Crypto-currency",
    author="Melchi Salins",
    author_email="melchisalins@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["requests>=2.22.0", "websockets==9.1"],
    include_package_data=True,
    zip_safe=True,
)
