import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="megachonker",
    version="0.2",
    author="Ana Fabela",
    author_email="ana.fabelah@gmail.com",
    description="Use megachonker for optimizing the backup of large files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anabanami/megachonker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    setup_requires=['setuptools', 'setuptools_scm'],
    install_requires=['tqdm'],
    scripts=['megachonker'],
)