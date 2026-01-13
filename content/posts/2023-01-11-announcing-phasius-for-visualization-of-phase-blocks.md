---
title: "Announcing Phasius for visualization of phase blocks"
date: 2023-01-11T13:40:40
draft: false
categories: ["Uncategorized"]
---

Long-read sequencing enables the phasing of variants and reads, i.e., separating those into two parental haplotypes. Without trio information, you will not be able to say which variant is inherited from which parent, but you will know which variants were inherited together. And this matters, e.g., for compound heterozygous variants and cis-regulatory variation. Phasing can work out across long distances but ends in the case of long nasty repeats (e.g., segmental duplications) or long regions without heterozygous variants.

I have developed [Phasius](https://github.com/wdecoster/phasius), a tool for visualizing phase blocks (continuously phased segments). It is a Rust tool with a binary you can [download ](https://github.com/wdecoster/phasius/releases/tag/v0.1.0)or get from [bioconda](https://anaconda.org/bioconda/phasius). The output is a HTML plot, with on the x-axis the genomic coordinates and on the y-axis one horizontal line per BAM/CRAM file, with interruptions (and change of color) for every line indicating the end of one phase block and the start of a new block.  A screenshot of an example can be found below, and a dynamic example to play with can be found [here](https://phasius.bioinf.be/phasius-example.html). Feedback appreciated!

![](/gigabaseorgigabyte/images/2023-01_newplot.png)