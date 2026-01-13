---
title: "Inferring the sex based on exome sequencing"
date: 2017-12-14T13:37:43
draft: false
categories: ["Coding", "Plotting", "Python"]
---

So today I came across the annoying issue that someone had not bothered to document the sex of samples, even when we generated exome sequencing data of those. So I wrote a script to figure this out based on coverage on the X and Y chromosomes, but not in [the pseudoautosomal regions](https://en.wikipedia.org/wiki/Pseudoautosomal_region).

The script can be found below and takes as input a directory of bams. Based on empirical observations I set some cut-offs to infer the sex based on the ratio between X and Y coverage, but your mileage may vary depending on your kit used for exome sequencing (we use Roche SeqCap EZ Exome v3.0). At the end, it also produces a plot showing the determined sexes and ambiguous samples with their identifiers.

![gender_plot_anonymized](/gigabaseorgigabyte/images/2017-12_gender_plot_anonymized.png)

 

https://gist.github.com/wdecoster/a4182f1e200bc6eb8f2f1643678aae53