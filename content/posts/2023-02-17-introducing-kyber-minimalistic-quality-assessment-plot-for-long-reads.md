---
title: "Introducing kyber: minimalistic quality assessment plot for long reads"
date: 2023-02-17T22:38:59
draft: false
categories: ["Uncategorized"]
---

I am releasing kyber today, and you can find all about it on [GitHub](https://github.com/wdecoster/kyber). 

In short, kyber produces a heatmap showing where the majority of your reads are. On the x-axis is the log transformed read length, on the y-axis the accuracy (optionally Phred-scaled). The axis ranges are fixed and therefore easier to compare various datasets. The intention is to have a minimalistic and fast impression of your dataset. 

Example below:

![](/gigabaseorgigabyte/images/2023-02_image.png)