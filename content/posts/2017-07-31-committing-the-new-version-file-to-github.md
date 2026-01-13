---
title: "Committing the new version file to GitHub"
date: 2017-07-31T00:00:52
draft: false
categories: ["development", "Python"]
---

As part of committing recently made changes to GitHub you also have to commit the changed [version.py](https://gigabaseorgigabyte.wordpress.com/2017/07/28/how-to-avoid-duplicating-your-package-version-number/) file. Perhaps this is overly lazy, but I wrote a small Python script called [bumpversion.py](https://github.com/wdecoster/bumpversion) to save myself just a few keystrokes per commit. When I prepared the setup.py to submit this script to PyPI I discovered someone else already made a far more complicated [bumpversion](https://pypi.python.org/pypi/bumpversion) package, so I decided to name mine bumpversionsimple.

This script will search for a version.py file in the subdirectories of the current directory. It will read the version.py file and create a commit message when committing the changes. Note that when it finds multiple version.py files (unexpected in a project directory!) it will just print out an error, do nothing and exit.

Installation is simple:

pip install bumpversionsimple

 

https://gist.github.com/wdecoster/41147faa0a5f81907062bb6a37596a6a