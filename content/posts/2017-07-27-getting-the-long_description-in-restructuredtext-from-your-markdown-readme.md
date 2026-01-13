---
title: "Getting the setup.py long_description in reStructuredText from your Markdown README"
date: 2017-07-27T22:40:05
draft: false
tags: ["Python"]
categories: ["Coding", "development"]
---

I write my README files for Python/GitHub projects in Markdown, which is quite easy and convenient. But the PyPi guidelines for projects require a README.rst file in "reStructuredText". The setup.py file also has a field for a "long description", which will get inserted on the Pypi project page,  see for example [this one for NanoPlot](https://pypi.python.org/pypi/NanoPlot).

UPDATE: TURNS OUT THIS WAS A REALLY BAD IDEA
By modifying the setup.py as I did I required all system to have pypandoc installed, to enable them to install my packages. So installations would fail without pypandoc installed. I just modified all my setup.py files :-)

To avoid having to keep README.rst and README.md in sync I searched a bit online and found a convenient solution: [pypandoc](https://pypi.python.org/pypi/pypandoc) for converting the README.md on the fly to an rst format, as shown below with code which goes in your setup.py:

https://gist.github.com/wdecoster/a5c277fe6f979da369276bfefedde76a

The full setup.py from NanoPlot is shown below. If yo u have suggestions for improvement I would be happy to hear them!

https://gist.github.com/wdecoster/9284972574a6e1a2d79c2071846d48b3