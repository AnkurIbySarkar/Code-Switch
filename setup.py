import codecs
import setuptools


setuptools.setup(
    name="codeswitch",
    version="1.1",
    long_description=codecs.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AnkurIbySarkar/codeswitch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.5',
    install_requires=[
        "transformers",
    ],
)
