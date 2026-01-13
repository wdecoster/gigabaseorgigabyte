---
title: "A Twitter bot to find the most interesting bioRxiv preprints"
date: 2017-08-08T16:09:26
draft: false
tags: ["bot", "preprints", "raspberry pi", "twitter"]
categories: ["Coding", "Python"]
---

TLDR: I wrote [a Twitter bot](https://twitter.com/PromPreprint) to tweet the most interesting bioRxiv preprints. Follow it to stay up to date about the most recent preprints which received a lot of attention.

https://twitter.com/PromPreprint/status/894922615508393988

The past few months have seen an explosion of life science research papers which are first posted as a preprint.  Statistics about preprints can be found on [prepubmed](http://www.prepubmed.org/monthly_stats/), of which I also took the image shown below. The majority of preprints is clearly on bioRxiv, with more than 1000 submissions each month.

![july_preprints](/gigabaseorgigabyte/images/2017-08_july_preprints.png)

The idea of posting your article as a preprint is quite simple: get your results out as fast as possible, without waiting months or years for a publication in a glamorous journal. And publishing on a preprint server doesn't prevent you from publishing in that glamorous journal afterwards, as is illustrated by the growing [list of journals which accept preprints.](https://en.wikipedia.org/wiki/List_of_academic_journals_by_preprint_policy) Preprints are not peer reviewed and perhaps you should be just a bit more critical when reading. Recent developments such as Oxford Nanopore sequencing and CRISPR genome editing show why preprints are necessary: technological advances happen so fast, by the time your article is through peer-review and published your results are already obsolete and outdated. Some perspectives on preprints have been discussed in blog posts, such as [What’s up with preprints?](https://smallpondscience.com/2017/07/24/whats-up-with-preprints/), [Biology's roiling debate over publishing research early](https://www.wired.com/story/biologys-roiling-debate-over-publishing-preprint-research-early/) and [The selfish scientist’s guide to preprint posting](https://nikokriegeskorte.org/2016/03/13/the-selfish-scientists-guide-to-preprint-posting/), among numerous more.

This post is not meant to discuss [all merits of preprints](http://asapbio.org/), but how to stay on top of the enormous flow of (perhaps) interesting articles. Because obviously, that amount of preprints is getting hard to follow and even harder is to find the really interesting articles between the 1000 submissions every month. It's a needle in a haystack problem. Intro [altmetric](https://www.altmetric.com/): [altmetrics](https://www.altmetric.com/about-altmetrics/what-are-altmetrics/) roughly tell you how much attention a paper/preprint received, by keeping track of all mentions and shares on twitter, blogs, news articles,...
So the hypothesis is: a preprint which gets a lot of attention (e.g. shares on Twitter) is probably a promising preprint worth reading. Based on this I wrote my Twitter bot.

Essentially, [my bot](https://twitter.com/PromPreprint) will:

	Monitor the preprints submitted to bioRxiv
	Check their altmetric score
	Tweet about the preprint if it's in the top 10% of altmetric scores in bioRxiv

To make sure the news is still hot when you get it, this checking is only performed during the first week after submission, which is a parameter I will have to evaluate.

The [code](https://github.com/wdecoster/PromisingPreprint) to achieve this is split into two scripts:

	getPreprintsAndSave.py will run hourly, check the bioRxiv RSS feed and save articles to a file
	checkScoreAndTweet.py will run daily, check the altmetric score of the saved articles, tweet if high enough and remove old entries from the file

Both scripts are added at the bottom of this post. I use my raspberry pi 3 to run these scripts using a crontab. I have included some logging, to figure out what goes wrong if my bot doesn't behave as expected. I've been thinking about the best method to store my data, but in the end, I just went with a flat text file containing doi, URL, title and date. Perhaps something else, such as an SQLite database or pickled list/dictionary might be better. Feel free to suggest how I can improve this!

 

 

https://gist.github.com/wdecoster/5d94bb3381b0a9420678cc4035a0e79e

https://gist.github.com/wdecoster/b28a6c77b266f3d80296c0826d1315fa