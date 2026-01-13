---
title: "The distribution of basecall quality scores"
date: 2017-07-08T13:44:26
draft: false
tags: ["Python"]
categories: ["Nanopore", "Plotting"]
---

I also investigated the Oxford Nanopore quality scores in some of my previous posts, and this post is a follow-up of those. Today I investigate the distribution of the basecall quality scores and how the mean and median per read behave.

At the bottom of this post is the script I used to generate the three plots below. It's not the fastest code (which is fine because I don't to run it too often) and it's quite memory-hungry (which is fine because I have access to a lot of RAM). It uses the aveQual function from [nanomath](https://github.com/wdecoster/nanomath) (also discussed [in my previous post](https://gigabaseorgigabyte.wordpress.com/2017/06/26/averaging-basecall-quality-scores-the-right-way/)) and a plotting function from [nanoplotter](https://github.com/wdecoster/nanoplotter), two packages I wrote for [NanoPlot](https://github.com/wdecoster/NanoPlot) and other scripts. Perhaps I should put writing the READMEs for those packages on [my Todoist](https://todoist.com/) (this app basically organises my work and life).

Anyway, I gather the quality scores from FAB48174 from the [cliveome](https://github.com/nanoporetech/ONT-HG1) data, recently basecalled using Albacore v1.1.1. This is not the latest version, but I believe it's sufficiently similar to the current state of the basecaller for this analysis. From those quality scores, I calculate the median and means per read and compare those in the bivariate plot below. The Pearson correlation coefficient (0.99) tells us the correlation is pretty decent, but it's clear from the plot that averages are higher than the medians, about one Phred score difference.

![MedianvsMeanQualityScores_kde](/gigabaseorgigabyte/images/2017-07_medianvsmeanqualityscores_kde1.png)

This can probably be explained by the distribution of all individual quality scores as shown in the plot below, in which it's clear that the Phred scores don't follow a Gaussian distribution. Does this argue that an arithmetic mean is not appropriate for quality scores, and the median would be a better choice?

![BaseCallQualityDistribution](/gigabaseorgigabyte/images/2017-07_basecallqualitydistribution2.png)

 

https://gist.github.com/wdecoster/592033ea178cd164f89a28b11493a44c