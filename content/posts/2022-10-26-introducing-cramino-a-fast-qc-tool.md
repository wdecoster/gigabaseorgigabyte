---
title: "Introducing Cramino: a *fast* QC tool"
date: 2022-10-26T13:46:55
draft: false
categories: ["Uncategorized"]
---

I am releasing [Cramino](https://github.com/wdecoster/cramino) today, my first Rust experience. Cramino is a faster replacement for NanoStat, and extracts features from cram and bam files that are useful for quality assessment of long read sequencing data, including read lengths and read identities. The default output looks like below (left), and is generated in 12 minutes for a decent PromethION run. Optional features include the calculation of a file checksum, determine the sex of the subject or presence of aneuploidies, provide metrics of the read phasing performance, export read lengths and identities in the Apache Arrow format for plotting in NanoPlot and NanoComp, and simple histograms like the one below (right). For installation and usage instructions (as simple as downloading a binary), please have a look at the [GitHub repository](https://github.com/wdecoster/cramino). Feedback much appreciated!

![](/gigabaseorgigabyte/images/2022-10_image.png)