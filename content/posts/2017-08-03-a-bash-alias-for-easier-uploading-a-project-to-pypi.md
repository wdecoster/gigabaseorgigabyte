---
title: "Convenient uploading of a project to PyPI using a bash alias"
date: 2017-08-03T23:54:30
draft: false
categories: ["development"]
---

Earlier I thought that [using pypandoc in your setup.py](https://gigabaseorgigabyte.wordpress.com/2017/07/27/getting-the-long_description-in-restructuredtext-from-your-markdown-readme/) was a great idea to solve the long_description and the README.rst, when you write your README in Markdown. Spoiler: it's a pretty terrible idea...

So:

	I have my README files in Markdown
	I would like to have them also in reStructuredText for PyPI submission
	I don't want to copy paste and edit those files
	I want to fill in the long_description in setup.py when uploading projects to PyPI

So the new solution is a bash alias:
alias pypush='rm -r dist/ *.egg-info/ ; pandoc --from=markdown --to=rst --output=README.rst README.md && python setup.py sdist && twine upload dist/*'
 

This appears to solve the problems listed above.
It starts with clearing up the directory from the previous 'upload', then executes [pandoc](https://pandoc.org/) for conversion of the README.md to README.rst (which I also added to my .gitignore), followed by creating the source distribution and uploading of the package. My setup.py (see below) opens the README.rst to get the long_description which is shown on the [PyPI webpage](https://pypi.python.org/pypi/NanoPlot/).

Getting quite efficient here!

https://gist.github.com/wdecoster/dade5e8160d772610bbf070e5b9360cb