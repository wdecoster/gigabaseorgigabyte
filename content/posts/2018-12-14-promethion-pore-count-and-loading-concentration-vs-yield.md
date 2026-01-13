---
title: "PromethION pore count and loading concentration vs yield"
date: 2018-12-14T11:05:44
draft: false
categories: ["Nanopore", "Plotting", "Python"]
---

Highly similar to my previous post [comparing read length and yield on PromethION](https://gigabaseorgigabyte.wordpress.com/2018/12/11/promethion-read-length-vs-yield/) I today checked the correlation between the pore count on the flow cell and the loading concentration with the yield. The code is highly similar and therefore not shown again. We do not see a strinking correlation between the loading molarity (in fmol) and the yield, but the number of pores on the flow cell, not surprisingly, seems to be a rather good indication of the obtained yield, with a few exceptions. However, this is also slightly confounded by the date of sequencing, as more recently both the flow cells and the yields have gotten better - which we aren't sure off that this correlation also has a causal component.

![](/gigabaseorgigabyte/images/2018-12_molarity_vs_yield.png)

![](/gigabaseorgigabyte/images/2018-12_pores_vs_yield.png)