from pathlib import Path
import re
from setuptools import setup, find_packages


TOP_DIR = Path(__file__).parent.resolve()

with open(TOP_DIR.joinpath("push_action/__init__.py"), "r") as handle:
    for line in handle.readlines():
        version = re.findall(r'__version__ = "(.*)"', line)
        if version:
            break
    else:
        raise RuntimeError("Could not determine version from push_action/__init__.py")

with open(TOP_DIR.joinpath("README.md")) as handle:
    README = handle.read()

with open(TOP_DIR.joinpath("requirements.txt")) as handle:
    REQUIREMENTS = handle.read()

setup(
    name="commit_and_push_to_protected_branch",
    version=version[0],
    url="https://github.com/augustonascimentos/commit_and_push_to_protected_branch",
    license="MIT",
    author="Augusto Nascimento",
    description="Remove branch protection temporarily, commit and return with protection.",
    long_description=README,
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires="requirements.txt",
    entry_points={"console_scripts": ["src=src.main:main"]},
)
