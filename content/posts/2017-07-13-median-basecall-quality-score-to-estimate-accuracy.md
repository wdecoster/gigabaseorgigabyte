---
title: "Median basecall quality score to estimate accuracy"
date: 2017-07-13T17:31:50
draft: false
tags: ["Python"]
categories: ["Nanopore", "Plotting"]
---

I've had a few posts already about basecall quality scores and how those compare to the percent identity of the reads. This post is again a short follow-up on those stories. Today I investigate whether the median basecall quality (Phred) score of the aligned fragments is a good or better estimator for the percent identity than the average. Since the quality scores don't follow a Gaussian distribution as I demonstrated [last week](https://gigabaseorgigabyte.wordpress.com/2017/07/08/the-distribution-of-basecall-quality-scores/), an arithmetic average may not be appropriate.

The plot below was generated from the same dataset as last week (FAB48174 basecalled using albacore v1.1.1) and aligned using bwa mem -x ont2d to hg19 (shame on me for not using hg38). The code for the feature extraction and plotting is at the bottom of the post, in which I also demonstrate how to extract metrics from a bam file using multiple threads. The script spends most of the time in the plotting, the feature extraction itself is very fast.

As you can see from the plot the correlation isn't excellent. What is striking (but not the first time that I see something like this) is the bimodal distribution of both percent identity and quality. The top percent identity is around 88%, which corresponds to a median Phred score of 18-19 which would theoretically indicate a 1.3-1.6% error rate, and as such not an accurate prediction of the accuracy. So, no, the median of the Phred scores is not a good metric.

![MedianvsPercentIdentity_kde.png](/gigabaseorgigabyte/images/2017-07_medianvspercentidentity_kde.png)

https://gist.github.com/wdecoster/2d86539fb62633e9c7386a0e28db2596