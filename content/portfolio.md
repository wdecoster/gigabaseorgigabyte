---
title: "Portfolio"
date: 2024-01-01
lastmod: 2026-11-22
draft: false
aliases:
  - /projects/
---

Software I have written and maintain, mostly for long-read sequencing data. Everything is open source; each entry links to its GitHub repository.

## Quality control and read processing

| Tool | What it does for you |
|------|----------------------|
| [NanoPlot](https://github.com/wdecoster/NanoPlot) / [nanoplotrs](https://github.com/wdecoster/nanoplotrs) | Plots and summary statistics to judge the quality of a nanopore or PacBio sequencing run. Available in Python (NanoPlot) and as a faster Rust implementation (nanoplotrs). |
| [NanoComp](https://github.com/wdecoster/nanocomp) | Compares multiple sequencing runs or samples side by side. |
| [cramino](https://github.com/wdecoster/cramino) | Very fast quality metrics for long-read BAM and CRAM files. Use this instead of the older [NanoStat](https://github.com/wdecoster/NanoStat). |
| [chopper](https://github.com/wdecoster/chopper) | Filters and trims long reads by quality, length and GC content. Use this instead of the older [NanoFilt](https://github.com/wdecoster/nanofilt). |

## Tandem repeats

| Tool | What it does for you |
|------|----------------------|
| [STRdust](https://github.com/wdecoster/STRdust) | Genotypes tandem repeats from long reads, including large expansions. |
| [inquiSTR](https://github.com/wdecoster/inquiSTR) | Genotypes short tandem repeats from long reads. |
| [trout](https://github.com/wdecoster/trout) | Finds tandem repeat outliers in a sample, based on repeat length and sequence. |
| [aSTRonaut](https://github.com/wdecoster/aSTRonaut) | Visualizes tandem repeats and their structure. |

## Other long-read tools

| Tool | What it does for you |
|------|----------------------|
| [phasius](https://github.com/wdecoster/phasius) | Visualizes phase block structure across many BAM, CRAM or VCF files at once. |
| [methplotlib](https://github.com/wdecoster/methplotlib) / [methplotlib-rs](https://github.com/wdecoster/methplotlib-rs) | Plots DNA methylation from nanopore data for a region of interest. Available in Python (methplotlib) and as a Rust port (methplotlib-rs). |

## Looking for more?

[NanoPack](https://github.com/wdecoster/nanopack) gives an overview of the NanoPlot family of tools, and all my public repositories are on [GitHub](https://github.com/wdecoster).
