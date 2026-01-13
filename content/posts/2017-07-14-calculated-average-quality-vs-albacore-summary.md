---
title: "Calculated average quality vs. Albacore summary"
date: 2017-07-14T15:28:41
draft: false
tags: ["Python"]
categories: ["Nanopore", "Plotting"]
---

I discussed [earlier](https://gigabaseorgigabyte.wordpress.com/2017/06/26/averaging-basecall-quality-scores-the-right-way/) the difference between a) the calculated per read average basecall quality and b) the quality score given by albacore in the sequencing_summary file. Today I had a closer look at this difference and for one dataset I calculated the average quality from the fastq file and compared that to the accompanying sequencing_summary.

The code I used is as usual at the bottom of the post. As before I use the aveQual function from [nanomath](https://github.com/wdecoster/nanomath) and a bivariate plotting function from [nanoplotter](https://github.com/wdecoster/nanoplotter). I first loop over the fastq file, create a dictionary with as keys the read identifiers and values the calculated average quality scores. Next, I use the Python [csv](https://docs.python.org/3.6/library/csv.html) module to parse the sequencing_summary, skip the header and in a loop extract the average qualities and add those to the dictionary.

As can be seen from the plot there is a subgroup of reads for which the 'calculated average' is equal to the 'albacore average', following the bisection of the plot. The majority of the reads however have a lower 'albacore average'. For the peak of the curves the calculated average is about 13-13.5, while the albacore average is below 12. So while both metrics are strongly correlated (Pearson R=0.95), there is a clear difference.

The read quality is intended as an estimator of the read identity, and at least in previous evaluations it appeared that the quality score is too ambitious and the read identity is lower than estimated by the quality. So at least, the albacore average is more "in the right direction" than the calculated average.

![scaled_AveQualvsSummary_kde](/gigabaseorgigabyte/images/2017-07_scaled_avequalvssummary_kde.png)

https://gist.github.com/wdecoster/bbd446ff59991e34684226d757f847f8