---
title: "Read length and coverage for regional assembly of ONT data"
date: 2026-11-23T09:00:00+01:00
draft: false
tags: ["assembly", "read length", "Oxford Nanopore", "Flye", "hifiasm", "benchmarking"]
categories: ["Bioinformatics"]
---

In [the previous post](/gigabaseorgigabyte/posts/2026-10-31-critical-length-revisited/) I looked at read length for structural variant discovery and left assembly for a follow-up. Here is a first part of it: assembling a single region of the genome, one haplotype at a time. This is how many regional studies work: take the reads that map to a locus, assign them to haplotypes, assemble each haplotype, and compare across samples. How long should the reads be, and how much coverage do you need?

**The short answer:** it looks like the SV answer, and none of it is a big surprise. A longer library N50 gives more haplotypes assembled as one contig, with Flye gaining little beyond an N50 of about 20 kb. Coverage matters at least as much as length. And for hifiasm, assembling all reads of a region together did clearly better than splitting them by haplotype first, at least with R10 reads and a library N50 up to about 20 kb. This is one sample and 71 regions, so the numbers are rough: a value for one condition is only accurate to about ±5 to ±10 percentage points, and I only draw conclusions from larger differences.

## Approach

The code is in [the same repository](https://github.com/wdecoster/critical-length-revisited), and the reads and truth are the same as before: public ONT R10.4.1 HG002 reads cut to a library N50 of 5 to 50 kb, subsampled to 20x and 30x. The truth is the HG002 Q100 assembly.

I picked 71 regions, most of them about 0.5 Mb: 20 plain regions, 20 segmental duplications, 15 tandem repeat regions, 15 with a large insertion, and the MAPT locus (1–1.6 Mb). For each region I took the reads that map to it, assigned them to the two haplotypes with DeepVariant and WhatsHap, assembled each haplotype with Flye (`--nano-hq`) or hifiasm (`--ont`), and aligned the result to the truth haplotype. I call a haplotype **complete** if one contig covers at least 95% of the truth haplotype. Per haplotype, the coverage is about half of the sample's.

<details>
<summary>The details</summary>

- The reads of a region are the cut pieces whose alignment overlaps the region plus 50 kb flanks. They were tagged by haplotype with WhatsHap, and split per haplotype.
- For comparison I also ran hifiasm on all reads of a region at once ("all reads", its own haplotype separation), and assigned reads to the truth haplotype they align to best (a ceiling that no real pipeline reaches).
- Library N50 values are 5, 10, 20, 30 and 50 kb, drawn from the read length distribution of a standard ligation library as in the previous post. Results are for one random draw of reads; a second draw at 20 kb N50 differed by 0 to 6 percentage points in every condition.
- With 71 regions, the fraction of complete haplotypes in one condition has a 95% interval of about ±5 to ±10 percentage points (mostly ±7 to ±9), and the difference between two conditions on the same regions about ±3 to ±10. The intervals are bootstrap intervals over regions.
- Each assembled haplotype is scored against the better-matching truth haplotype, so the two haplotypes of an assembly could in principle both match the same one. Counting each truth haplotype only once lowers the fraction of complete haplotypes by at most 3 points in any mode, so this does not change the comparisons.

</details>

## Results

### Library N50 and coverage

![Fraction of haplotypes assembled as one contig against the read N50 of the library, for Flye and hifiasm at 20x and 30x](/gigabaseorgigabyte/images/2026-11_regional_n50.png)

| Library N50 | Flye, 20x | Flye, 30x | hifiasm, 20x | hifiasm, 30x |
|---|---|---|---|---|
| 5 kb | ~25% | ~60% | ~10% | ~55% |
| 10 kb | ~60% | ~75% | ~25% | ~75% |
| 20 kb | ~75% | ~80% | ~45% | ~75% |
| 30 kb | ~75% | ~85% | ~45% | ~80% |
| 50 kb | ~80% | ~85% | ~60% | ~90% |

*Fraction of haplotypes assembled as one contig covering the region (71 regions, two haplotypes each; reads split by haplotype as a regional pipeline would). Rounded to 5 points: the 95% interval of each value is about ±5 to ±10 points.*

The clear things in this table are the steep rise from 5 to 20 kb, and the effect of coverage. Going from 20x to 30x with Flye gains about 35 points at 5 kb N50 (interval 26 to 43) and 18 points at 10 kb (11 to 24), and about 6 to 7 points from 20 kb on. At 20x, Flye is clearly ahead of hifiasm at the shorter N50 values, and at 30x the two are similar. Beyond 20 kb, Flye's values (75% to 85%) change by less than I can resolve. hifiasm at 20x still seems to be gaining up to 50 kb, from 45% at 20 kb to 60%.

If the choice is between more depth and longer reads, depth looks like the cheaper one for this question: for hifiasm, 30x at 10 kb N50 (about 75%) did better than 20x at 50 kb (about 60%).

The base accuracy of the assemblies also rises with the N50: the median QV is about 31 at 5 kb and 38 at 50 kb (30x, both assemblers).

<details>
<summary>The details</summary>

- By region class (Flye, 30x, 5 kb to 50 kb N50): plain regions about 80% to 100%, tandem repeats about 65% to 100%, large insertions about 55% to 95%, and segmental duplications about 45% to 60%. hifiasm shows the same order, with segmental duplications at about 40% to 75%.
- The MAPT locus is not assembled as a single contig under any condition. hifiasm covers 89–100% of the truth haplotypes with contigs of about 0.7 Mb at 5 kb N50 up to 1–1.5 Mb at 30–50 kb (the truth haplotypes are about 1.2 and 1.6 Mb); Flye stops at about 0.6 Mb for every N50, so read length helps hifiasm here and not Flye.
- Fixed read lengths at 30x: Flye about 75% (10 kb) to 85% (100 kb); hifiasm about 70% (10 kb) to 85% (50 kb). The 100 kb condition has 22x rather than 30x because there are not enough ultra-long reads, and is labelled accordingly in the repository.
- The QV is estimated from the identity of the assembly to the truth haplotype.

</details>

### Splitting the reads or not

![Fraction of haplotypes assembled for hifiasm on all reads, on reads split by haplotype, and on reads split by the truth haplotype](/gigabaseorgigabyte/images/2026-11_regional_split.png)

In most regional pipelines the reads of a region are split by haplotype before assembly, because each haplotype is then assembled on its own. hifiasm can instead take all reads and separate the haplotypes itself. That did better:

| Library N50 | 20x | 30x |
|---|---|---|
| 5 kb | +35 (27 to 44) | +14 (4 to 24) |
| 10 kb | +32 (22 to 42) | +13 (6 to 20) |
| 20 kb | +18 (10 to 25) | +8 (0 to 15) |
| 30 kb | +13 (6 to 21) | +1 (−6 to +9) |
| 50 kb | +10 (4 to 16) | +2 (−4 to +8) |

*Gain in complete haplotypes, in percentage points (95% interval), of hifiasm on all reads over hifiasm on reads split by haplotype.*

The gain is clear at 20x for every N50, and at 30x up to about 20 kb. From 30 kb at 30x there is no clear difference. At 20x and a short N50, all reads even beat the ceiling in which every read is assigned to its true haplotype.

My explanation, which I did not test further, is that splitting halves the depth hifiasm sees in all the sequence the two haplotypes share, which is most of the region. The cost is in phasing: hifiasm's own haplotypes switch somewhat more often than those of the split reads (2.5 against 1.7 switches per haplotype at 5 kb, 0.25 against 0.20 at 50 kb; 30x).

<details>
<summary>The details</summary>

- This is for hifiasm only; I did not run Flye on all reads together. All reads here are R10; R9 was not tested.
- A hifiasm assembly of all reads was scored as two haplotypes against the better-matching truth haplotype, as for the other modes.
- Raw values (rounded to 5 points): at 30x, all reads 70%, 85%, 85%, 85%, 90% for 5, 10, 20, 30 and 50 kb, against 55%, 75%, 75%, 80% and 90% for split reads; at 20x, all reads 45%, 55%, 60%, 60%, 70% against 10%, 25%, 45%, 45%, 60%.

</details>

### Hard regions and phasing

Regions with segmental duplications stay hard: about 45% to 60% complete with Flye at 30x, against about 80% to 100% for plain regions, and MAPT is never assembled as one contig. Read length alone does not solve those.

One pitfall if you measure phasing: the switch error rate that `yak trioeval` reports (run with k-mers of the two truth haplotypes) is about 3% to 6% at every N50, even when every read is assigned to the right haplotype. Almost all of it is single-base differences at long heterozygous homopolymers, where the assembly carries the other haplotype's length, and yak counts each as two switches. Counting only switches between stretches of at least 10 haplotype-specific k-mers, real phase switches per assembled haplotype fall about tenfold from 5 to 50 kb (1.7 to 0.15 with hifiasm at 30x). I also tried joining the phase blocks with SHAPEIT4 and a reference panel (HPRC); this halved phase switches at 5–10 kb, but I found no clear gain in complete haplotypes.

## Recommendation

- **An N50 of about 20 kb is a reasonable target** for regional assembly with Flye; I could not resolve a gain beyond it. For hifiasm, longer still seems to help up to 50 kb at 20x. Treat this as a rough guide.
- **Get the coverage first.** 20x to 30x gains as much as several steps in N50 at the shorter end, and hifiasm at 20x with short reads mostly fails.
- **With R10 reads and hifiasm, try assembling all reads of the region together** before building a read-splitting step, certainly below 20 kb. Phasing is somewhat better when splitting, but completeness suffers.
- **Do not expect the hard regions to be solved by read length alone.**
- **If you benchmark phasing, count switches between stretches, not yak's raw rate.**

## Limitations

- One genome (HG002), one random draw of reads for most conditions, 71 regions. A value for one condition is accurate to about ±5 to ±10 percentage points, so differences below roughly 10 points are not reliable, and I did not try to rank conditions that close.
- Regions are around 0.5 Mb (the MAPT locus is larger), not whole chromosomes, and I did not compare with genome-scale assemblies.
- The truth is the HG002 Q100 assembly, and the phasing comparison with a reference panel is for one panel and one sample.
- Assembly-based SV discovery and genome-scale assembly are still to do.

## Try it yourself

The workflow, including the region selection, truth extraction and evaluation, is in the repository above. The figures are made by `scripts/blog_figures_regional.py` from the per-assembly evaluation tables.

Feedback and suggestions are, as always, welcome.
