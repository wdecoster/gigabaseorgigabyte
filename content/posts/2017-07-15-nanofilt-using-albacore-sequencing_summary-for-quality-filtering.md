---
title: "NanoFilt using albacore sequencing_summary for quality filtering"
date: 2017-07-15T20:49:22
draft: false
categories: ["Nanopore", "Python"]
---

Due to a [discrepancy between the quality scores calculated from the reads and those from the sequencing_summary.txt from albacore](https://gigabaseorgigabyte.wordpress.com/2017/07/14/calculated-average-quality-vs-albacore-summary/) I added an option to [NanoFilt](https://github.com/wdecoster/nanofilt) to filter using the qualities specified in the sequencing_summary.

NanoFilt now (v1.1.0) also optionally takes a --summary flag for the sequencing_summary file. As a nice bonus, it's also faster! This added a new dependency to NanoFilt, my [nanoget](https://github.com/wdecoster/nanoget) module which performs extraction of metrics from fastq files, bam files and sequencing_summary files and returns all information in a convenient pandas DataFrame. For fast lookup of the quality scores this DataFrame is converted to a dictionary linking the read identifier with the quality score.

https://twitter.com/AnneLiseDMDu/status/886482350812446720

 

https://twitter.com/AnneLiseDMDu/status/886378005907390464