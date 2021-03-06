from __future__ import print_function

import distutils.spawn
from setuptools import find_packages
from setuptools import setup
import shlex
import subprocess
import sys


github_slug = "wkentaro/video-cli"
name = "video-cli"
version = "0.4.0"


if sys.argv[1] == "release":
    if not distutils.spawn.find_executable("twine"):
        print(
            "Please install twine:\n\n\tpip install twine\n", file=sys.stderr
        )
        sys.exit(1)

    commands = [
        "git pull origin master",
        "git tag v{:s}".format(version),
        "git push origin master --tag",
        "python setup.py sdist",
        "twine upload dist/{:s}-{:s}.tar.gz".format(name, version),
    ]
    for cmd in commands:
        subprocess.check_call(shlex.split(cmd))
    sys.exit(0)


def get_long_description():
    with open("README.md") as f:
        long_description = f.read()

    try:
        import github2pypi

        return github2pypi.replace_url(
            slug=github_slug, content=long_description
        )
    except Exception:
        return long_description


def get_install_requires():
    install_requires = []
    with open("requirements.txt") as f:
        for req in f:
            install_requires.append(req.strip())
    return install_requires


setup(
    name=name,
    version=version,
    packages=find_packages(exclude=["github2pypi"]),
    install_requires=get_install_requires(),
    description="Command line tools for quick video editing.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Kentaro Wada",
    author_email="www.kentaro.wada@gmail.com",
    url="http://github.com/{:s}".format(github_slug),
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    entry_points={
        "console_scripts": [
            "video-retime=video_cli.retime:main",
            "video-togif=video_cli.togif:main",
            "video-trim=video_cli.trim:main",
            "video-tile=video_cli.tile:main",
            "video-toimg=video_cli.toimg:main",
            "video-tovideo=video_cli.tovideo:main",
            "video-resize=video_cli.resize:main",
            "video-fromimg=video_cli.fromimg:main",
        ]
    },
)
