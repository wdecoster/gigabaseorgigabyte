---
title: "Nanopore ActivityMaps"
date: 2017-03-15T16:48:25
draft: false
tags: ["NanoPlot", "Python"]
categories: ["Nanopore", "Plotting"]
---

In February Keith Robison suggested in his post [Could Hermione Tackle MinION Yield Variability?](http://omicsomics.blogspot.be/2017/02/could-hermione-tackle-minion-yield.html) it would be useful to get a physical overview of the sequenced reads per channel. This script should visualise which channels have been very productive and which didn't contribute at all. I thought this was a neat idea, and since I am working on a python script (NanoPlot) to create various plots from Nanopore sequencing data I also included this.

For sharing the result early I wrote some minimal code to create this "Activity Map". Currently, the code parses the filename of the fast5 files to get the channel information. The only argument to the script is a directory containing fast5 files, which will be searched recursively. This strategy is the fastest, but this will obviously break if something is changed in the naming convention. The script needs about 30 seconds for 500k reads, of which most time is spend loading modules. This code is currently meant to be used after a run, but changes can be made to run it live and update the image periodically. As in a heat map, darker green means more reads while the x and y-axis give the channel coordinates on the flowcell.

Usage: python Nanoplot_ActivityMap.py --fast5 /path/to/fast5/directory/

I generated three examples based on data from the CliveOme from Clive Brown, using runs FAB48174, FAB48453 and FAF02814 of which the results are below and the code can be found at the bottom of the page.

I welcome all feedback!

[gallery ids="69,68,67" type="slideshow"]

https://gist.github.com/wdecoster/cbbbe1cf50c925a2df4fd8d5beee5ac9