import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OctoEverywhereAPI", # Replace with your own username
    version="1.0.3",
    author="mytja",
    description="A Unoffical API for OctoEverywhere",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mytja/OctoEverywhereAPI",
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
