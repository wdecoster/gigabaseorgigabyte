---
title: "PromethION sequencing in Antwerp in 2018"
date: 2018-12-07T09:48:35
draft: false
categories: ["Nanopore", "Plotting"]
---

We started using PromethION about a year ago, but the good flow cells started arriving from February onwards. Below I have an overview of our runs so far, generated using [NanoComp](https://github.com/wdecoster/nanocomp). I'll blog more about these later if I have the time, but I'm finishing my PhD this month... The plots below show the yield in gigabase and the log transformed  read length distribution per run, sorted by date of sequencing.

Our yield is quite variable, but the worst runs can be explained by bad input DNA quality. Garbage in, garbage out. Our best run so far was about 116Gbase. We haven't been specifically optimizing our DNA extraction, as we are not interested in megabase reads which are without doubt interesting for assembly, but not necessarily that valuable for human genetics using alignment.  We also see that shearing DNA to 10-20kb using MegaRuptor is highly beneficial for our yield - but this requires a more thorough investigation and optimization. We hope to get flongles soon for things like this... We also use BluePippin to remove short fragments from our library.

![](/gigabaseorgigabyte/images/2018-12_yield_cropped.png)

![](/gigabaseorgigabyte/images/2018-12_logreadlength_cropped.png)

Finally, I'd like to remind you that we have made quite some PromethION human genome sequencing data from NA19240 [available](https://gigabaseorgigabyte.wordpress.com/2018/05/24/promethion-human-genome-na19240/) for download. Some of our results have also been described in two preprints:

[Structural variants identified by Oxford Nanopore PromethION sequencing of the human genome](https://www.biorxiv.org/content/early/2018/10/14/434118)

[Accurate characterization of expanded tandem repeat length and sequence through whole genome long-read sequencing on PromethION.](https://www.biorxiv.org/content/early/2018/11/15/439026)