import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data_string_search",
    version="0.0.2",
    author="Saurabh",
    author_email="saurabhrane.m@gmail.com",
    description="Package to advance search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saurabhranem/python_library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'fuzzywuzzy',
        'fuzzywuzzy[speedup]',
    ]
)