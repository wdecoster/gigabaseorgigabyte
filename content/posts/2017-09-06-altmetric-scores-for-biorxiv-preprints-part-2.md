---
title: "Altmetric scores for bioRxiv preprints, part 2"
date: 2017-09-06T10:00:08
draft: false
tags: ["altmetric", "preprints"]
categories: ["Coding", "Plotting", "Python"]
---

This post is part of the series starring altmetric attention scores and bioRxiv preprints, see also the earlier post about [my Twitter bot](https://gigabaseorgigabyte.wordpress.com/2017/08/08/a-twitter-bot-to-find-the-most-interesting-biorxiv-preprints/), [getting the altmetric scores](https://gigabaseorgigabyte.wordpress.com/2017/08/20/getting-altmetrix-scores-for-all-biorxiv-preprints/) and [part 1 of the analysis](https://gigabaseorgigabyte.wordpress.com/2017/08/28/altmetric-scores-for-biorxiv-preprints-part-1). Today I'll have a look at the top 10% altmetric scores and how fast the preprint got that score. These are the articles about which my bot would tweet. But note that this 90th percentile is the state of the scores when I gathered the data, and not when the preprint itself was posted. So it's not entirely accurate, but it will at least tell us something about the "dynamics" of getting attention. Remember that I require for my twitter bot that the preprints reach their score in the first week after publication, a parameter I will evaluate today.

Like last week I start with loading the data. The 90th percentile corresponds to a score above 31.3, so that's our cut-off to select the part of interest. The 'winners' DataFrame contains the historical data of 1323 articles, with a mean and median score of respectively 75.2 and 48.8. Note that I also transposed the DataFrame for convenience. Subsequently, I change the index from categorical labels to an array of pandas Timedelta objects. The constructor interprets '1d' as 1 day, but the the labels 'w', m' and 'y' are not understood so I write those explicit as a number of days.

https://gist.github.com/wdecoster/1803ee3ea6b1f2ca590463910e5449d1

Now I want to make a "spaghetti plot" out of this to get an idea of the evolution of the scores through time. For the first spaghetti plot, I limit the scores to 1000 to get a broad overview. I have added a dotted line showing the required cut-off. This shows that for many preprints the scores reach a plateau quite quickly. Also, for quite a lot (401) of preprints, the high attention score isn't even reached in the first year. It perhaps takes longer before other papers start citing the preprint.

Due to the missing data points (for example between 1 week and 1 month) the curve is not smooth at all and it's hard to estimate when, truly, the preprint got its attention.

https://gist.github.com/wdecoster/f0f1836cf6cd76d651a8c2effa25b018

![Spaghetti1](/gigabaseorgigabyte/images/2017-08_spaghetti1.png)

Let's zoom in on the first three months by tweaking the code above a bit. The result shows that my parameter of reaching the 90th percentile in the first week is unreasonable since many preprints will still get a higher score up to the first month or even later. Therefore I decide to change this parameter to the first month, to give preprints a bit more time to get traction and reach more people.

https://gist.github.com/wdecoster/9c4787d53b1a67fd39b8cddda6d34558

![Spaghetti2](/gigabaseorgigabyte/images/2017-08_spaghetti2.png)