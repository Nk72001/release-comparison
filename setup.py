from setuptools import setup, find_packages

setup(
    name="release-comparison",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
         'requests>=2.26.0'   # Adding requests library with a minimum version
    ],
    author="NK72001",
    author_email="neha.kendhuli@bitloka.com",
    description="A library for comparing software releases",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Nk72001/release-comparison.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)