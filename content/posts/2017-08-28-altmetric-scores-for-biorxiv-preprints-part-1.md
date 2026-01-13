---
title: "Altmetric scores for bioRxiv preprints, part 1"
date: 2017-08-28T10:00:43
draft: false
tags: ["altmetric", "preprints"]
categories: ["Plotting", "Python"]
---

This post is following my earlier posts about my [Twitter bot for interesting preprints](https://gigabaseorgigabyte.wordpress.com/2017/08/08/a-twitter-bot-to-find-the-most-interesting-biorxiv-preprints/) and how to get [altmetric scores for all bioRxiv preprints](https://gigabaseorgigabyte.wordpress.com/2017/08/20/getting-altmetrix-scores-for-all-biorxiv-preprints/). In this post, I want to take a first look at the obtained data. I'll do this using the Python pandas module.

When working with pandas DataFrames interactively it's convenient to set the display.width option to accommodate your screen width. The default is 80, but this results in a lot of row wrapping. I could set this without problem to 200.
import pandas as pd
pd.set_option('display.width', 200)
I saved the data as a tab separated text file, which can be loaded using the read_csv function.
df = pd.read_csv("Altmetric-biorxiv.txt", sep="\t", header=0)
A quick set of summary statistics can be calculated using the .describe() method. I specified I also want the 90th percentile, because that's the cut-off I chose for my Twitter bot before considering a preprint interesting enough to tweet about.
df.describe(percentiles=[0.90])
This tells me, among much more metrics, that I have data from 13261 preprints. The mean and median altmetric score is respectively 15.5 and 7.9. Preprints with a score above 31.3 are in the 90th percentile. The maximum altmetric score is a whopping 2615.8.

Let's have a look at the top of the list by sorting the DataFrame and getting the 10 highest scoring preprints. Since I didn't keep the titles for all preprints I'll query these again and add the titles to the DataFrame. Since the titles are longer than the default column width I change this option as well.
top = df.sort_values("score", ascending=False).head(10)[["doi", "score"]].reset_index()
from altmetric import Altmetric
a = Altmetric()
top["title"] = [a.doi(d)['title'] for d in top["doi"]]
pd.set_option('max_colwidth', 120)
![TopPreprints](/gigabaseorgigabyte/images/2017-08_toppreprints.png)

Interestingly enough, 7 out of these preprints have not been published in a 'real journal' (yet). The remaining 3 are published in PLOS (Computational) Biology. This list contains a few rather controversial papers, including 'getting cancer from cell phone radiation', 'sex differences in human brain' and 'no evidence of horizontal gene transfer in the tardigrade genome'. It makes sense these get a lot of attention. The list also contains 4 articles with meta-science: articles about other articles.

These top scoring preprints are real outliers in the data, as can be seen in the histogram below. The y-axis (containing the number of preprints) is log-transformed to make the smaller bins with high scores visible. The blue line shows the current cut-off to get in the top 10%. The distribution is clearly asymmetric: many preprints get a low score and just a few get a lot of attention.
df["score"].plot(kind='hist', log=True, color="#4CB391", bins=25)
plt.xlabel('Altmetric score')
plt.ylabel('Log transformed number of preprints')
plt.title('Distribution of altmetric scores')
plt.axvline(x=31.3)
plt.show()
 

 

![DistributionOfScores](/gigabaseorgigabyte/images/2017-08_distributionofscores3.png)

When dropping all preprints with a score above 500 (only 11 preprints) the curve becomes more informative and shows that the happy 10% aren't that far off of the majority of all preprints.
low = df[df["score"] 
![DistributionOfScores_lower](/gigabaseorgigabyte/images/2017-08_distributionofscores_lower.png)

Further analysis is for another day...