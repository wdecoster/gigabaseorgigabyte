---
title: "Briefly evaluating SVIM"
date: 2019-01-11T14:18:50
draft: false
tags: ["structural variants"]
categories: ["Coding", "Nanopore", "Python"]
---

Although it was available for a longer time already, in December the long read structural variant (SV) caller [SVIM](https://github.com/eldariont/svim) was published as a [preprint](https://www.biorxiv.org/content/early/2018/12/13/494096). As I have published about [tools for long read sequencing](https://www.biorxiv.org/content/early/2018/10/14/434118) before I decided to also take a look at SVIM.

I started from reads of our [NA19240 PromethION](https://gigabaseorgigabyte.wordpress.com/2018/05/24/promethion-human-genome-na19240/) genome aligned using minimap2 to GRCh38, and compared with variants shared by [Chaisson](https://www.biorxiv.org/content/early/2018/06/13/193144). I didn't time it, but SV calling using svim was reasonably quick. Of note, SVIM currently does not output genotypes and only informs you about the presence of a variant, without providing the zygosity of the position. The length pattern of the SVs is not entirely as expected, as it misses the characteristic peaks at 300 and 6000 bp, corresponding to SVs involving respectively Alu and L1 elements.

![](/gigabaseorgigabyte/images/2019-05_image.png)

The tool identified 3.7 million variants, of which 3.2 > 50 bp (the commonly used definition of a structural variant).  This is of course far more than what we would expect for a human genome (about 25000-30000 variants).  However, svim also adds quality scores to their calls, so I used these to filter, with increasing stringency, and create a precision-recall graph. The code for this procedure is available [here](https://github.com/wdecoster/nano-snakemake/blob/master/extra_scripts/precision-recall-curve-qualities.py) and uses mainly [SURVIVOR](https://github.com/fritzsedlazeck/SURVIVOR), pandas, cyvcf2, and matplotlib. Without filtering the tool reaches 80% recall but almost zero precision. With filtering on quality scores this precision increases with a modest loss in recall. At 60% recall, about 70% of the variants are accurate, a performance roughly similar to other structural variant callers in my published comparison. The decision of the author to output all variants and have the user sort those out makes sense, however, it would probably be more realistic to not write those variants which have really a terrible quality score. However, setting cutoffs is difficult and invariably a tradeoff between sensitivity and specificity.

![](/gigabaseorgigabyte/images/2019-05_image-1.png)

So, another structural variant caller for long reads. It is clear we haven't seen the last of these, and the field will take a while until the most optimal and mature tool has been found and refined.