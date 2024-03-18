# python -m venv .
# pip install -r requirements.txt
# python -m venv venv
# source venv/bin/activate
# .\venv\Scripts\activate.bat
# pip freeze | Out-File -Encoding UTF8 requirements.txt

from setuptools import setup, find_packages


print(open("requirements.txt", encoding="utf-8").read().splitlines())

setup(
    name="SHDW-Management-Bot",
    version="0.1",
    description="Simple team management bot for SHDW eSports",
    author_email="robonaut5v@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ItzReality/shdw/tree/Management-UI",
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=[
        dep.lstrip("\ufeff")
        for dep in open("requirements.txt", encoding="utf-8").read().splitlines()
    ],
    classifiers=[
        # Choose your license as you wish
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.12",
)
