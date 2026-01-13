---
title: "Oxford Nanopore basecall quality scores"
date: 2017-06-12T08:30:26
draft: false
categories: ["Nanopore", "Plotting"]
---

A recent switch in Oxford Nanopore basecaller software (albacore v1.0.1) substantially improved the per-base quality scores, as mentioned in [a previous post.](https://gigabaseorgigabyte.wordpress.com/2017/05/10/per-base-sequence-content-and-quality-new-basecaller/) I wondered if those quality scores are accurate. As shown below, the average base quality of a read is above 16. These scores are Phred-scaled quality scores, meaning they correspond to the -10*log10(Probability of incorrect base call). As such, a Phred score of 10 indicates a 1/10 probability of an incorrect base or a 90% accuracy. See also [this page on Wikipedia](https://en.wikipedia.org/wiki/Phred_quality_score). Similarly, a score of 16 indicates an accuracy of ~97.49%.![PerBaseSequenceQuality](/gigabaseorgigabyte/images/2017-05_perbasesequencequality.png)

A proxy for the accuracy of the technology would be the percent identity of a sample aligned to the reference genome, implying that we assume that our sample is sufficiently similar to the reference genome. Obviously, this individual will have differences due to polymorphisms. The [Genome of the Netherlands](http://www.nature.com/ng/journal/v46/n8/full/ng.3021.html) Project identified roughly 3M variants per individual, which is not too far from [an earlier study on fewer individuals](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0059494). Therefore,  considering a 3.2Gb genome, the upper limit of the percent identity is about 99.9%.

Shown below is one of the plots created by [NanoPlot](https://github.com/wdecoster/NanoPlot), plotting the per read average basecall quality versus its percent identity. The data used here is from the [Cliveome](https://github.com/nanoporetech/ONT-HG1/blob/master/CONTENTS.md), generated in November 2016. The basecalling was repeated with the most recent Albacore version, followed by alignment to GRCh37 with bwa mem -x ont2d. This plot shows there is a considerable spread on both the percent identity and average basecall quality, with a reasonable correlation between the two as expected. Most reads are situated at an average read quality of 20, with a percent identity of approximately 88%. But a score of 20 would mean an accuracy of 99%, so this is clearly an overconfident quality score.

 

![scaled_PercentIdentityvsAverageBaseQuality_kde](/gigabaseorgigabyte/images/2017-06_scaled_percentidentityvsaveragebasequality_kde1.png)