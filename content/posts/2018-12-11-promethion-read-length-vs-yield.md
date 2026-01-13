---
title: "PromethION Read length vs yield"
date: 2018-12-11T15:09:42
draft: false
categories: ["Nanopore", "Plotting"]
---

It has been suggested by other PromethION users that there is an inverse correlation between read length of the library and the yield of the run. We usually shear our DNA to 10-20kb, so we don't really have a lot of observations of libraries with very long DNA. Based on [our current runs](https://gigabaseorgigabyte.wordpress.com/2018/12/07/promethion-sequencing-in-antwerp-in-2018/) there is no obvious (inverse) correlation. Some of our worst runs, however, did have a longer read length, but simultaneously also had lower DNA quality. I extracted the read length N50 value and the yield from the NanoStats.txt file using the command below and added a header (note that you could also grep for both patterns simultaneously). The code snippet to generate that plot, using pandas, is at the bottom of the post.  No obvious correlation here, but we definitely need more observations to draw solid conclusions.

paste \  yield_vs_N50.txt

![](/gigabaseorgigabyte/images/2018-12_yield_vs_n50.png)

https://gist.github.com/wdecoster/92883a2ea0fde11de3af32241c5b686f