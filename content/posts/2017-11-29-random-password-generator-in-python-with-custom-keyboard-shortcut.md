---
title: "Random password generator in Python with custom keyboard shortcut"
date: 2017-11-29T22:19:50
draft: false
categories: ["Coding", "Python"]
---

I use different, randomly generated passwords for all my accounts. I have used a website to generate those before, but today I wrote a small script to handle this job. The main idea is based on [this StackOverflow question](https://stackoverflow.com/q/7479442/6631639), which I adapted and extended to suit my needs. It's probably not completely cryptographically safe as pointed out by some reactions in the thread linked above, but it is for sure good enough for my application.

This script can be executed as a command line script and if executed with -v it will print a password from letters and characters, and a second one also including symbols. Optionally the length can be changed using -l.

More useful, I set a [custom keyboard shortcut](https://help.ubuntu.com/stable/ubuntu-help/keyboard-shortcuts-set.html) to execute this script, and the call to pyperclip.copy() will load the generated password in my clipboard, so I can conveniently paste it, wherever I need it.

https://gist.github.com/wdecoster/be980a22ca3b8a9a1e9ad11460e44828