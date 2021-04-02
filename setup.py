import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OctoEverywhereAPI", # Replace with your own username
    version="1.0.1.1",
    author="mytja",
    description="Get session cookie for simple login onto your OctoEverywhere Printer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mytja/AliExpressAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests'
    ],
    python_requires='>=3',
)