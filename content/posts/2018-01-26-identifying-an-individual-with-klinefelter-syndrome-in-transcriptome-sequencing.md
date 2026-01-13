---
title: "Identifying an individual with Klinefelter syndrome in transcriptome sequencing"
date: 2018-01-26T00:01:46
draft: false
categories: ["Plotting", "R", "transcriptomics"]
---

In my previous post, I showed how to [infer the sex of individuals from transcriptome sequencing.](https://gigabaseorgigabyte.wordpress.com/2018/01/02/inferring-the-gender-based-on-transcriptome-sequencing/) I applied this to a different dataset, and the result (shown below) has a remarkable outlier: sample 34.

The title is already a big spoiler: it turns out that this individual has [Klinefelter syndrome](https://en.wikipedia.org/wiki/Klinefelter_syndrome) (47,XXY), a male with two X chromosomes. XIST shouldn't be expressed in males, but we also validated this finding using qPCR. In addition, we found genomic evidence supporting this observation since we genotyped an STR marker on chromosome X showing two alleles, which can only happen if this individual has two X chromosomes. According to Wikipedia the frequency of this chromosomal anomaly is "1-2 subjects per every 1000 males", so that's actually quite frequent...

Mystery solved!

 

![GenderSpecificExpression](/gigabaseorgigabyte/images/2018-01_genderspecificexpression.jpeg)