import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RYLR896Py", # Replace with your own username
    version="0.0.1",
    author="Konstantinos Kamaropoulos",
    author_email="k@kamaropoulos.com",
    description="A simple library to interact with the RYLR896 LoRa Module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)