#USAGE NOTES
#
# Make a Pypi release tarball with:
# 
#   python3 setup.py sdist
# 
# Upload to test PyPi with:
# 
#   twine upload --repository-url https://test.pypi.org/legacy/ dist/* 
# 
# Install from test Pypi with:
#   
#   pip install --index-url https://test.pypi.org/simple/ {name of program}
#   
#Upload to real PyPI with:    
# 
#   twine upload dist/*
# 
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="megachonker",
    version="0.3",
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