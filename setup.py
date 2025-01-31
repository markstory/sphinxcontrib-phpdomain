import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
    requirements = f.read()

long_desc = """
This package provides a Sphinx extension for documenting PHP projects.

PHP Domain supports following objects:

* Global variable
* Global function
* Constants
* Namespaces

    * Functions
    * Class

* Class

    * Class constant
    * Instance methods
    * Static methods
    * Properties

* Enums
"""

setup(
    name="sphinxcontrib-phpdomain",
    version="0.13.0",
    url="https://github.com/markstory/sphinxcontrib-phpdomain",
    download_url="http://pypi.python.org/pypi/sphinxcontrib-phpdomain",
    license="BSD",
    author="Mark Story",
    author_email="mark@mark-story.com",
    description="Sphinx extension to enable documenting PHP code",
    long_description=long_desc,
    project_urls={
        "Documentation": "https://markstory.github.io/sphinxcontrib-phpdomain/",
    },
    classifiers=[
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Sphinx :: Domain",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    platforms="any",
    dependency_links=[],
    namespace_packages=["sphinxcontrib"],
    packages=find_packages(exclude=["test*"]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
)
