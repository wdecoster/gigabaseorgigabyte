---
title: "Getting the edit distance from a bam alignment: a journey"
date: 2017-04-14T15:22:33
draft: false
categories: ["Nanopore", "Plotting"]
---

A relevant parameter when looking at sequencing and alignment quality is the edit distance to the reference genome, roughly equivalent to the accuracy of the reads. (Roughly, because we ignore true variants between the sample and reference). The edit distance or Levenshtein distance can be defined as the number of single letter (nucleotide) changes that have to be made to one string (read) for it to be equal to another string (reference genome). Since the error profile of Nanopore sequencing is dominated by insertions and deletions, the edit distance isn't just the number of single nucleotide mismatches.

This technology results in a wide range of read lengths, therefore I scale the edit distance to the length of the aligned fragment. Longer reads shouldn't get penalised more than shorter reads. It's important to take the alignment length and not the read length since the ends of reads can be clipped substantially by the aligner, sometimes tens of kb.  The experiments below were done using [MinION data from the human genome in a bottle sample NA12878](https://github.com/nanopore-wgs-consortium/NA12878).

My scripts are in Python, so I'll add some code snippets to this post. For parsing bam files and extracting the relevant bits of information, I use [pysam](https://github.com/pysam-developers/pysam) which is pretty convenient and [well-documented](http://pysam.readthedocs.io/en/latest/). Those snippets are not the full script, but just a minimal example to get the job done. A full example of the code is at the bottom of the post.

Getting this information from an alignment done using [bwa mem ](http://bio-bwa.sourceforge.net) is trivial since bwa sets the NM bam tag which is an integer with precisely what I need: the edit distance. A function to extract the NM tag using a list comprehension is added below.

https://gist.github.com/wdecoster/308c31006323175bed555d159d42641a

For aligners such as [GraphMap](https://github.com/isovic/graphmap) this is less trivial since the NM tag is not set. However, another tag comes to the rescue: the MD tag, which stores a string containing matching numbers of nucleotides and non-matching nucleotides. Interesting information about the MD tag can be found [here](https://github.com/vsbuffalo/devnotes/wiki/The-MD-Tag-in-BAM-Files). I found it a quite tough representation of the read to wrap my head around, which resulted in some wrong interpretations.

My first naive implementation counted the number of matching nucleotides (the integers in the MD string) and subtracted those matches from the total alignment length to get the number of mismatched nucleotides. The list comprehension is quite long, but essentially I split the MD string on all occurrences of A, C, T, G or ^ (indicating a deletion) and sum the obtained integers. This sum is subtracted from the aligned read length and divided by the same.

https://gist.github.com/wdecoster/886e9b013c08523cf45cea89b6855950

As a sanity check I looped over a bwa mem aligned bam file to extract both the scaled NM tag and scaled MD-derived edit distance and plot those against each other, for which you can see the code below followed by the images. Between gathering the information from the bam file in lists and plotting the data I convert my lists to a numpy array and create a pandas DataFrame (see bottom of post). Since the first plot is rather overcrowded I also added a kernel density estimation to get a better idea of the density of the dots.

https://gist.github.com/wdecoster/74fc4905450ad528cfcbc07f69dd466e

[gallery ids="138,137" type="rectangular" link="file"]

The Pearson correlation coefficient is not too bad, but obviously, we want to get exactly the same as the NM tag. It's clear that my implementation of getting the edit distance from the MD tag returns an underestimation of the edit distance. After thinking a while I decided to [create a question on biostars](https://www.biostars.org/p/246784/) where [Santosh Anand](https://www.biostars.org/u/24747/) joined my quest. He suggested counting the mismatches in the MD string, rather than the matches, which I implemented below. So this time I split the MD string on all numbers and sum the length of the mismatched nucleotides. The plots obtained by this approach are shown below the code.

https://gist.github.com/wdecoster/252dd039efaef332405be4c08dd3680e

[gallery ids="171,170" type="rectangular" link="file"]

That's an improvement, but we're not yet there. At this point Santosh asked for a few examples of reads which showed a clear deviation in NM and MD-derived edit distance. I wrote a function to do just that, which prints out:

	The NM tag
	The MD tag derived edit distance
	The MD tag
	The CIGAR string

https://gist.github.com/wdecoster/5f1c10401b1d567a2fd132deb90b80cd

This is an example of a read showing a clear mismatch between the NM tag and the MD-derived edit distance.

73
34
21G1C3A1T1A2G4A8T2G4A2G0G0G19^G2G10T6C1A2A0G0G0A5T6^GA5A0G0C0C1G3A5A6C1C2
1684H20M3I7M3I10M1I5M2I1M1I1M3I6M1I4M1I13M2I5M4I3M7I6M1D6M2I1M2I26M1I3M1I2M1I3M2D16M1I6M3I10M10942H

The hero on my quest then found that we were still missing the insertions, which are not present in the MD tag but can only be counted by parsing the CIGAR string. I copied the image below from his post.

![CountingInsertions](/gigabaseorgigabyte/images/2017-04_countinginsertions-e1492174493947.png)

So my successful implementation also parses the CIGAR string to get the insertions and add those to the mismatches. In my final code piece below I show the full code of my evaluation of the edit distances, including some multiprocessing code to process chromosomes in parallel and converting the lists to numpy arrays in a pandas DataFrame.

The kernel density estimate plot crashes on an exact correlation, so this time you only get the scatter plot. Problem solved and everyone lived happily ever after.

Big thanks to Santosh Anand!

![EditDistancesCompared_scatter](/gigabaseorgigabyte/images/2017-04_editdistancescompared_scatter.png)

 

https://gist.github.com/wdecoster/a0ca604306b5778a7167f705c597ee38