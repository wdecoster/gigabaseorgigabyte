---
title: "Removing accidental 2D/1D^2 reads from an alignment"
date: 2020-04-18T13:58:30
draft: false
tags: ["structural variants"]
categories: ["Coding", "Nanopore"]
---

In [surpyvor](https://github.com/wdecoster/surpyvor) I collect scripts which can be helpful for structural variant analysis. Today I added a "purge2d" subcommand to remove accidental 2D/1D^2  nanopore reads from a BAM file. Most typically we do 1D ligation preps, but in some cases the complement fragment is sequenced directly after the template and not recognized as separate molecules, as what used to be 2D sequencing (with a hairpin) and is nowadays 1D^2 sequencing (without covalent link). Typically this complement read also has a much lower quality, since the template read starts refolding and pulling the strand through at the trans side, and as such complicating accurate basecalling.

The principle of sequencing both strands can increase the base accuracy (since you have two observations) but is in our case not what we are looking for. Worse, this events mimics an inverted duplication. For sufficient coverage and germline variant detection this is not much of an issue, since these events are rare. However looking at somatic or low-coverage variants this might result in quite some noise.

![](/gigabaseorgigabyte/images/2020-04_image.png)

As such this script extract supplementary alignments which are overlapping to the primary alignment on the other strand, and removes those from a bam file. Of course I do not exclude the possibility of actually having inverted duplications in the sample of interest, so therefore if multiple of these reads happen in within 500 bp from each other those are kept, just to be sure we are not removing any signatures of an actual structural variant.

At this moment it's pretty slow, as I'm not exploring any parallelization. Pull requests are very much welcome, and please let me know what you think!