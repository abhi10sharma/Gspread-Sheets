from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "gspread10", # name of our package...
    version = "0.0.1",
    author = "Abhishek Sharma",
    author_email = "abhishekbangana1847@gmail.com",
    description = "Package which helps us to read the data from google sheets ",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/abhi10sharma/Gspread-Sheets",
    license = "MIT",
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
    ],
    install_requires = ["gspread", "oauth2client", "pandas", "matplotlib"]
)