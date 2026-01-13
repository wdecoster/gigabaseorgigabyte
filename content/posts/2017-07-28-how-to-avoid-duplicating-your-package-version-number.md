---
title: "How to avoid duplicating your package version number using a version.py file"
date: 2017-07-28T10:00:45
draft: false
tags: ["Python"]
categories: ["Coding", "development"]
---

I thought it was rather annoying to specify the version of your package both in the tool itself and in your setup.py, so I searched the internet for solutions and below I'll explain how I set it up.

I have a version.py file in my project folder and this is the only spot where I keep my version number, which only contains the following.

__version__ = "0.16.1"

The script itself contains the following line to import the version number, making __version__ a variable in my script where I can easily use to report (and log) the version number:

from .version import __version__

In my setup.py I have the following line, which will also make the __version__ variable available for uploading the script to Pypi:

exec(open('mypackage/version.py').read())

 

Some useful resources on how to organize package development are the following:

	[PyPA Packaging and Distributing Projects](https://packaging.python.org/tutorials/distributing-packages/)
	The accompanying [sample project on GitHub](https://github.com/pypa/sampleproject)
	Guidelines on [Open Sourcing a Python Project the Right Way](https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/)