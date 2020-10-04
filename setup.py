from setuptools import setup, find_packages


setup(
    name='pydomain',
    version='0.1',
    author="kokokuo",
    author_email="v6610688@gmail.com",
    description="This is a domain-driven design tatical building blocks package for python.",
    packages=find_packages(exclude=["docs", "tests*"]),
    install_requires=[
        "sutoppu"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ]
)
