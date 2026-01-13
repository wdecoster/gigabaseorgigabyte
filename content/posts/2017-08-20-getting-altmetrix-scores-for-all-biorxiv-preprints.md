---
title: "Getting Altmetric scores for all bioRxiv preprints"
date: 2017-08-20T16:20:31
draft: false
tags: ["altmetric", "preprints"]
categories: ["Python"]
---

I recently wrote [a Python bot to tweet about bioRxiv preprints](https://gigabaseorgigabyte.wordpress.com/2017/08/08/a-twitter-bot-to-find-the-most-interesting-biorxiv-preprints/) as soon as they reach the top 10% of attention for bioRxiv on altmetric. To make sure I made some right choices there I want to analyse the altmetric scores and their history of all bioRxiv preprints.

As far as I know, the bioRxiv database doesn't have a convenient API, but I could [get a list of all DOIs](https://github.com/OmnesRes/prepub/blob/master/biorxiv/biorxiv_licenses.tsv) from [Jordan 'OmnesRes' Anaya](https://github.com/OmnesRes), who is the author and maintainer of [PrePubMed](http://www.prepubmed.org/), a searchable database of preprints from various servers. The script I used to query altmetric is added at the bottom of this post. I executed the code as:
python altmetric-query.py biorxiv-dois.txt
Since the file with the DOIs was not hardcoded in the script I could also do quick tests with bash "process substitution" to query just a few DOIs and see if the code is working:
python altmetric-query.py 
An alternative would be to have the script read from stdin:
head -n 5 biorxiv-dois.txt | python altmetric-query.py
 

The code starts with writing out the header for the extracted metrics, and then I queried the Altmeric database in a loop. I added plenty of time between the calls to the API (10 seconds) to make sure I didn't hammer their server. As such this script took rather long to run but as it was not urgent this was not a real problem.

Annoyingly, the returned dictionary did not always contain the same keys in the "cited_by" categories. To get an idea what the most important fields in this category are I had a look at the keys returned for the [ExAC preprint](http://www.biorxiv.org/content/early/2015/10/30/030338). I guess I will have the most important channels then. When a field was not returned by the Altmetric API I assumed this to be 0.

I added a bit of error handling, but it turned out that this was not necessary, but it's always better to be safe than sorry.

The analysis of the data is for another post!

https://gist.github.com/wdecoster/bdeb5db29683f073b0170d0864e3411c