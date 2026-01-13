---
title: "A handy bash alias for compressing and indexing vcf files"
date: 2019-05-22T09:15:28
draft: false
categories: ["bioinformatics"]
---

I often have a ton of vcf files, which I would like to compress using bgzip and index using tabix, which is necessary for many downstream steps such as bcftools concat. I grew tired of always typing the same command, so I wrote the following bash alias, which uses [gnu parallel ](https://www.gnu.org/software/parallel/) and is part of my .bash_aliases file. 

alias vcfzip="ls *.vcf | parallel --bar 'bgzip {} && tabix {}.gz'"

When I'm in a directory with files that need to be compressed I can simply execute vcfzip and all files will get compressed and indexed, together with a friendly progress bar.