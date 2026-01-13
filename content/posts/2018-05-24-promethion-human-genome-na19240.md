---
title: "PromethION human genome NA19240"
date: 2018-05-24T15:30:30
draft: false
categories: ["Nanopore"]
---

TLDR: we sequenced a human genome, NA19240, to 80x coverage using the Oxford Nanopore PromethION. The data is freely available on ENA.

We have been sequencing on Oxford Nanopore PromethION since February. Our main interest is in structural variation in the context of neurodegenerative diseases such as Alzheimer Disease and Frontotemporal Dementia, but for benchmarking and tool development we have sequenced the Yoruba reference genome NA19240 to 80x coverage (258Gigabases) using 5 flowcells, a Yoruban individual part of the HapMap and 1000 genomes project and well documented ([Steinberg et al 2016](https://www.biorxiv.org/content/early/2016/08/02/067447https://www.biorxiv.org/content/early/2016/08/02/067447),  [Chaisson et al 2017](https://www.biorxiv.org/content/early/2017/09/23/193144), and many more).

The ENA project ID is [PRJEB26791](https://www.ebi.ac.uk/ena/data/view/PRJEB26791), the most recent basecalls (guppy 1.4.0) can be found [here](https://www.ebi.ac.uk/ena/data/view/SAMEA4724698). We have also generated two runs on MinION for comparison, which are also available.
Summary

Run
DNA shearing
BluePippin size selection
Library prep kit
Yield [Gbase]
ENA accession

P1
unsheared
>10kb
LSK109
59
[ERR2631600](https://www.ebi.ac.uk/ena/data/view/ERR2631600)

P2
MegaRuptor 20kb
>8kb
LSK109
69
[ERR2631601](https://www.ebi.ac.uk/ena/data/view/ERR2631601)

P3
unsheared
>10kb
LSK109
29
[ERR2631602](https://www.ebi.ac.uk/ena/data/view/ERR2631602)

P4
unsheared
>10kb
LSK108
29
[ERR2631603](https://www.ebi.ac.uk/ena/data/view/ERR2631603)

P5
MegaRuptor 20kb
>6kb
LSK109
72
[ERR2631604](https://www.ebi.ac.uk/ena/data/view/ERR2631604)

M1
unsheared
>10kb
LSK109
4.8
[ERR2683660](https://www.ebi.ac.uk/ena/data/view/ERR2683660)

M2
unsheared
>10kb
LSK109
7.9
[ERR2683661](https://www.ebi.ac.uk/ena/data/view/ERR2683661)

Plots
The plots below were generated using [NanoComp](https://github.com/wdecoster/nanocomp) and [NanoPlot](https://github.com/wdecoster/NanoPlot).

![NanoComp_total_throughput](/gigabaseorgigabyte/images/2018-05_nanocomp_total_throughput1.png)

![NanoComp_log_length](/gigabaseorgigabyte/images/2018-05_nanocomp_log_length1.png)\

![TimeQualityViolinPlot](/gigabaseorgigabyte/images/2018-05_timequalityviolinplot.png)