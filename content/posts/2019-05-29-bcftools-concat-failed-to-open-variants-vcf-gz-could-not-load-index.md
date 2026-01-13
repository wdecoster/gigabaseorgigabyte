---
title: "bcftools concat: Failed to open variants.vcf.gz: could not load index"
date: 2019-05-29T09:10:24
draft: false
tags: ["bcftools concat"]
categories: ["bioinformatics"]
---

If you are like me and like to massively parallelize jobs then you may come across the following, initially cryptic error when using bcftools concat with thousands of vcf files:

bcftools concat -a *.vcf.gz | bcftools sort -o all_variants.vcfFailed to open a_certain_variant_file.vcf.gz: could not load index

I believe the problem is that too many files are opened. For each vcf also the index (.tbi) file is opened, which turns out to be more than the number of files your operating system allows you to open. You can check that using ulimit -u, which in my case is 1024. You could see if your system permits increasing that limit, or you could do the merging in batches. First I will split the list of vcf files in a few files using the unix tool split, well below our ulimit -n / 2 (500 vcf files in my example). Then I merge and sort each batch separately, [compress and index using a handy bash alias](https://gigabaseorgigabyte.wordpress.com/2019/05/22/a-handy-bash-alias-for-compressing-and-indexing-vcf-files/), and finally merge the intermediate files:

ls *.vcf.gz | split -l 500 - subset_vcfsfor i in subset_vcfs*; do bcftools concat -a $(cat $i | tr '\n' ' ') | bcftools sort -o ${i}.vcf; donevcfzip bcftools concat -a subset_vcfs*.vcf.gz | bcftools sort -o all_merged.vcf.gz -O z

After this, all what is left is cleaning up some intermediate files.