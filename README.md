# snakemake-gatk

Snakemake wrappers for GATK.

## Requirements

- [GATK 4.0.8.1](https://software.broadinstitute.org/gatk/download/)
- Executable `gatk` in `$PATH`

## Recommended

To utilize [public resources](https://console.cloud.google.com/storage/browser/genomics-public-data/resources/broad/hg38/v0) of Broad Institute, using **hg38 reference genome** (which can also be downloaded at [public resources](https://console.cloud.google.com/storage/browser/genomics-public-data/resources/broad/hg38/v0)) is higly recommended. The link may get outdated by any time, so please refer to the official website of GATK to get the latest version of the resources. (Last updated: 2018.08.23)

## Available wrappers

- **reference**: manipulate FASTA references
  - [create-sequence-dictionary](gatk/reference/create-sequence-dictionary): wrapper for [CreateSequenceDictionary (Picard)](https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.3.0/picard_sam_CreateSequenceDictionary.php)
- [**mutect2**](gatk/mutect2): call somatic SNPs and indels
  - [tumor-normal](gatk/mutect2/tumor-normal): wrapper for [Mutect2](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_mutect_Mutect2.php)
- **cnv**: copy number variant discovery
  - [create-read-count-panel-of-normals](gatk/cnv/create-read-count-panel-of-normals): wrapper for [CreateReadCountPanelOfNormals](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_CreateReadCountPanelOfNormals.php)
  - [denoise-read-counts](gatk/cnv/denoise-read-counts): wrapper for [DenoiseReadCounts](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_DenoiseReadCounts.php)
- **variant-filtering**: reduce the number of false-positive variant calls
  - [create-somatic-panel-of-normals](gatk/variant-filtering/create-somatic-panel-of-normals): wrapper for [CreateSomaticPanelOfNormals](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_mutect_CreateSomaticPanelOfNormals.php)
- **preprocessing**: preprocess aligned read files
  - [mark-duplicates](gatk/preprocessing/mark-duplicates): wrapper for [MarkDuplicates](https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.4.0/picard_sam_markduplicates_MarkDuplicates.php)
  - [base-recalibrator](gatk/preprocessing/base-recalibrator): wrapper for [BaseRecalibrator](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_BaseRecalibrator.php)
  - [apply-bqsr](gatk/preprocessing/apply-bqsr): wrapper for [ApplyBQSR](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_ApplyBQSR.php)
- **intervals**: manipulate list of genomic intervals
  - [preprocess-intervals](gatk/intervals/preprocess-intervals): wrapper for [PreprocessIntervals](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_PreprocessIntervals.php)
- **coverage**: count reads
  - [collect-read-counts](gatk/coverage/collect-read-counts): wrapper for [CollectReadCounts](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_CollectReadCounts.php)
- **misc**: miscellaneous
  - [index-feature-file](gatk/misc/index-feature-file): wrapper for [IndexFeatureFile](https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.3.0/org_broadinstitute_hellbender_tools_IndexFeatureFile.php)
