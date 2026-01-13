---
title: "Per base sequence content and quality"
date: 2017-04-24T23:17:15
draft: false
tags: ["NanoPlot", "Python"]
categories: ["Nanopore", "Plotting"]
---

I wrote a script to produce QC plots analogous to the "￼Per base sequence quality" and ￼"Per base sequence content" from [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/) for Nanopore sequencing data. Since there is no fixed read length this representation is less straightforward, so it's necessary to make a selection of the data. My script starts from a fastq file, which I parse using [Biopython SeqIO](http://biopython.org/wiki/SeqIO). I start with making a histogram of the read lengths, to select the bin containing the most reads to represent the data of the entire run. This is probably not the most perfect approach and I welcome suggestions.

Below are the modules used in the script and some minimal [argparse](https://docs.python.org/3/library/argparse.html) code for working conveniently with command line arguments. The rest of the functions are organised by the main()function. The full code of the script is at the bottom of the post.

https://gist.github.com/wdecoster/8c671251863dcdbfb170ed564e75f183

I start with looping over the fastq file, using a list comprehension to get the length of all reads in a numpy array.

https://gist.github.com/wdecoster/74cd5e72b42e0c5f99d91b9bc9ae3628

Based on these lengths a histogram is made using matplotlib. Matplotlib produces a histogram by passing the data to [numpy.histogram](https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html), which I also use to return the number of reads per bin and the bin edges. Using a different algorithm for creating bins would result in more or less bins, and would yield different results in the downstream functions. The histogram is shown below. The index of the bin containing the most reads (about 4800) is found with np.argmax(), which is then used to get the edges of this bin.

https://gist.github.com/wdecoster/4f32e03fb6c888979fb162d0c884dd00

![LengthHistogram.png](/gigabaseorgigabyte/images/2017-04_lengthhistogram.png)

In the following function, I loop a second time over the fastq file, this time to extract information of the reads belonging to the lucky bin. Using a list comprehension both the sequence and integer quality scores are returned in a tuple per read.

https://gist.github.com/wdecoster/97a7fb07fe147c0b8b4a4edec0afbbe5

The read information is separately passed to the next functions, in the first the nucleotide diversity or fractions per position are plotted. The python base function zip() creates a generator in which the first nucleotides of each reads are combined in a new list, e.g. [[A,C,G,T],[C,G,A,A],[G,C,C,T]] becomes [[A,C,G],[C,G,C],[G,A,C], [T,A,T]], and as such per position the fraction per position can be calculated.  The zip() function will stop when the shortest element (or read) is exhausted, and therefore all plots are limited to the shortest read length in this bin, which is just less than 800 nucleotides (and therefore rather short for Nanopore sequencing data). The unpack/splat (*) operator is required to unpack the list fqlists in the separate lists.

https://gist.github.com/wdecoster/cabdcea287892d76ec21ad82fa4718de

The resulting plot is shown below. It's clear that the first nucleotides are non-random, suggesting a bias in the fragmentation or base calling. Another striking observation is the overrepresentation of thymidine bases in the entire read, which is unlikely.

![PerBaseSequenceContent](/gigabaseorgigabyte/images/2017-05_perbasesequencecontent.png)

Generating a plot with the average quality per position is done using a similar function.

https://gist.github.com/wdecoster/576e571c6471f16333d4673599d75fad

The result of this is shown below, showing a uniform quality score for most of the read but a remarkable low quality at the start of the reads. This seems like a good suggestion for cropping a part of the read, about 30-40 nucleotides.

![PerBaseSequenceQuality](/gigabaseorgigabyte/images/2017-05_perbasesequencequality.png)

The full code of this script is shown below:

https://gist.github.com/wdecoster/7cad6080950fa1e3ae3eaeeac4f6ae4d