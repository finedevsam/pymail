import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pymail", # Replace with your own username
    version="1.0.0",
    author="Samson Ilemobayo",
    author_email="ilemobayosamson@gmail.com",
    description="Python Library to send email with template and send files via email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/finedevsam/pymail.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    
    ],
    python_requires='3.x',
    install_requires=[
        "Jinja2",
    ],
)