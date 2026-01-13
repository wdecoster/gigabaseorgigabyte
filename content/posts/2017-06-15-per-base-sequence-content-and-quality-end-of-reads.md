---
title: "Per base sequence content and quality (end of reads)"
date: 2017-06-15T08:30:45
draft: false
categories: ["Nanopore", "Plotting"]
---

After my earlier [posts](https://gigabaseorgigabyte.wordpress.com/2017/05/10/per-base-sequence-content-and-quality-new-basecaller/) investigating the sequence content and quality at the start of Oxford Nanopore sequencing reads, I also wanted to include some code to look at the end of reads. These functions are part of the unfinished tool [nanoQC,](https://github.com/wdecoster/nanoQC) in which I want to replicate some of the plots made by [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/).

Creating the same plots as shown earlier was rather trivial since this involves just reversing the lists of quality scores and nucleotides. However, I also wanted to include all 4 plots together in one figure, and I spent a few hours to figure out how to deal with the legend. The secret sauce consists of creating an additional ax object where you want the legend, add the legend there and then make the additional ax object invisible, as suggested in [this stackoverflow answer.](https://stackoverflow.com/a/11153040/6631639)

These plots show that also the end shows a lower quality and biased nucleotide composition, although to a lesser extent compared to the begin of the read. This is again a good argument in favour of using the headcrop and tailcrop options in [NanoFilt.](https://github.com/wdecoster/nanofilt)

The full code can be found on [GitHub](https://github.com/wdecoster/nanoQC) (which will receive further updates) and (frozen) at the bottom of this post.

![PerBaseSequenceContentQuality.png](/gigabaseorgigabyte/images/2017-06_perbasesequencecontentquality.png)

https://gist.github.com/wdecoster/aa6087c6b98fb1ca5e33b894696f2ff2