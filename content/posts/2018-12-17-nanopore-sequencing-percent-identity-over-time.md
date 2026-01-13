---
title: "Nanopore sequencing: percent identity over time"
date: 2018-12-17T12:22:46
draft: false
categories: ["Nanopore", "Plotting", "Python"]
---

My [NanoPlot ](https://github.com/wdecoster/NanoPlot)tool includes plots showing the decline in base call quality and sequencing speed over time, see below. 

![](/gigabaseorgigabyte/images/2018-12_quality_over_time.png)

![](/gigabaseorgigabyte/images/2018-12_speed_over_time.jpg)

Sequencing speed reduction is presumably because the ATP in the fuel mix gets consumed, or pores start wearing out. However, I wondered if this lower quality near the end of the run was also reflected in lower percent identity, or it was just misjudged by the basecaller. But this requires getting data from the alignment and from a summary file, as the time at sequencing is lost after alignment. NanoPlot can create a [pickle ](https://docs.python.org/3/library/pickle.html)file to save the pandas DataFrame with all extracted features, so I did this for a summary file and the corresponding bam file. The code for processing and plotting is below, and indeed we see a decline in percent identity over time. Maybe running your flow cell as long as possible isn't going to get you much more decent data? 

![](/gigabaseorgigabyte/images/2018-12_percentIdentityOverTimeViolin.png)

https://gist.github.com/wdecoster/bd9ac9baa8f561952332ce756b0ec1e0