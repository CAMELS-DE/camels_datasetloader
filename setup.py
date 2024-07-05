from setuptools import setup, find_packages


def requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def version():
    with open("./camels_datasetloader/__version__.py") as f:
        code = f.read()
    loc = dict()
    exec(code, loc, loc)
    return loc["__version__"]


setup(
    name="camels_datasetloader",
    description="Load data from CAMELS-DE datasets",
    author="Alexander Dolich",
    author_email="alexander.dolich@kit.edu",
    install_requires=requirements(),
    license="GPL-3.0",
    version=version(),
    packages=find_packages()
)
