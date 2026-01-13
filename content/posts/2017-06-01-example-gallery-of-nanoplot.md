---
title: "Example gallery of NanoPlot"
date: 2017-06-01T21:38:19
draft: false
tags: ["NanoPlot", "Python"]
categories: ["Nanopore", "Plotting"]
---

I am developing [NanoPlot](https://github.com/wdecoster/NanoPlot), a python package for plotting various aspects of Nanopore sequencing data (fastq) and alignments (bam). It's a python script, heavily using the seaborn package for creating plots. The package is available on [GitHub](https://github.com/wdecoster/NanoPlot) and I welcome all feedback and suggestions!

In this post, I will show some examples of plots. The data is from the [Cliveome](https://github.com/nanoporetech/ONT-HG1) flowcell FAB48453, after repeating the basecalling with albacore v1.1.0 followed by filtering and trimming using the NanoPlot companion script [NanoFilt](https://github.com/wdecoster/nanofilt).

 

![scaled_OutliersRemoved_Downsampled_HistogramReadlength](/gigabaseorgigabyte/images/2017-06_scaled_outliersremoved_downsampled_histogramreadlength.png) This plot shows a simple histogram with read N50 metric.

 

![scaled_Log_Downsampled_HistogramReadlength](/gigabaseorgigabyte/images/2017-06_scaled_log_downsampled_histogramreadlength1.png) Similar to the plot above, but here with log10 transformed read lengths.

 

![scaled_OutliersRemoved_Downsampled_LengthvsQualityScatterPlot_kde](/gigabaseorgigabyte/images/2017-06_scaled_outliersremoved_downsampled_lengthvsqualityscatterplot_kde.png) This bivariate plot shows with a kernel density estimate the read length compared to the average read basecall Phred quality.

![scaled_Log_Downsampled_LengthvsQualityScatterPlot_kde](/gigabaseorgigabyte/images/2017-06_scaled_log_downsampled_lengthvsqualityscatterplot_kde.png) This plot contains the same as above, but again with a log10 transformation on the read lengths.

![scaled_Log_Downsampled_LengthvsQualityScatterPlot_hex](/gigabaseorgigabyte/images/2017-06_scaled_log_downsampled_lengthvsqualityscatterplot_hex.png) This plot is the same as the previous, but instead of a kernel density estimate here hexagonal bins are used to show the distribution of the data.

![scaled_OutliersRemoved_Downsampled_MappingQualityvsReadLength_kde](/gigabaseorgigabyte/images/2017-06_scaled_outliersremoved_downsampled_mappingqualityvsreadlength_kde.png) Here is a comparison of the read length with the mapping quality of those reads after alignment using bwa mem -x ont2d. Clearly there is a subgroup of small reads showing very low mapping quality.

![scaled_Log_Downsampled_MappingQualityvsReadLength_kde](/gigabaseorgigabyte/images/2017-06_scaled_log_downsampled_mappingqualityvsreadlength_kde.png) This is the same plot as above but with a log scale on the read length.

![scaled_MappingQualityvsAverageBaseQuality_kde](/gigabaseorgigabyte/images/2017-06_scaled_mappingqualityvsaveragebasequality_kde.png) This plot compares the average basecall quality of reads with their mapping quality, clearly showing that there is a subgroup of low quality reads which are essentially useless. Keep in mind that the worst quality reads were removed from this dataset prior to alignment.

![scaled_PercentIdentityvsAverageBaseQuality_kde](/gigabaseorgigabyte/images/2017-06_scaled_percentidentityvsaveragebasequality_kde.png) This plot compares the percent identity (the edit distance to the reference genome scaled by the read length) with the read quality. The majority of the reads have a percent identity of about 85-90%, but with a long tail to identities of ~60%.

![scaled_PercentIdentityvsAlignedReadLength_kde](/gigabaseorgigabyte/images/2017-06_scaled_percentidentityvsalignedreadlength_kde.png) This plot compares the read length (log10 transformed) with the percent identity.

![scaled_AlignedReadlengthvsSequencedReadLength_scatter](/gigabaseorgigabyte/images/2017-06_scaled_alignedreadlengthvssequencedreadlength_scatter.png) In this graph the read length is compared with the aligned read length, showing an expected line on the bisection but also showing reads which are not fully aligned due to softclipping.