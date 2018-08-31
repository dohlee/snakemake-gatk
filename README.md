# snakemake-gatk

Snakemake wrappers for GATK.

## Requirements

- [GATK 4.0.8.1](https://software.broadinstitute.org/gatk/download/)
- Executable `gatk` in `$PATH`

## Recommended

To utilize [public resources](https://console.cloud.google.com/storage/browser/genomics-public-data/resources/broad/hg38/v0) of Broad Institute, using **hg38 reference genome** (which can also be downloaded at [public resources](https://console.cloud.google.com/storage/browser/genomics-public-data/resources/broad/hg38/v0)) is higly recommended. The link may get outdated by any time, so please refer to the official website of GATK to get the latest version of the resources. (Last updated: 2018.08.23)

## Available wrappers

- **cnv**: copy number variant discovery
  - [create-read-count-panel-of-normals][create-read-count-panel-of-normals]: wrapper for [CreateReadCountPanelOfNormals](CreateReadCountPanelOfNormals)
  - [denoise-read-counts](gatk/cnv/denoise-read-counts): wrapper for [DenoiseReadCounts][DenoiseReadCounts]
- **coverage**: count reads
  - [collect-read-counts][collect-read-counts]: wrapper for [CollectReadCounts][CollectReadCounts]
  - [get-pileup-summaries][get-pileup-summaries]: wrapper for [GetPileupSummaries][GetPileupSummaries]
- **intervals**: manipulate list of genomic intervals
  - [preprocess-intervals][preprocess-intervals]: wrapper for [PreprocessIntervals][PreprocessIntervals]
- **misc**: miscellaneous
  - [index-feature-file][index-feature-file]: wrapper for [IndexFeatureFile][IndexFeatureFile]
- [**mutect2**][mutect2]: call somatic SNPs and indels
  - [tumor-normal][tumor-normal]: wrapper for [Mutect2 with tumor & normal sample][Mutect2 with tumor & normal sample]
  - [tumor-only][tumor-only]: wrapper for [Mutect2 with single sample][Mutect2 with single sample]
- **preprocessing**: preprocess aligned read files
  - [mark-duplicates][mark-duplicates]: wrapper for [MarkDuplicates][MarkDuplicates]
  - [base-recalibrator][base-recalibrator]: wrapper for [BaseRecalibrator][BaseRecalibrator]
  - [apply-bqsr][apply-bqsr]: wrapper for [ApplyBQSR][ApplyBQSR]
- **qc**: quality control
  - [calculate-contamination][calculate-contamination]: wrapper for [CalculateContamination][CalculateContamination]
- **reference**: manipulate FASTA references
  - [create-sequence-dictionary][create-sequence-dictionary]: wrapper for [CreateSequenceDictionary (Picard)][CreateSequenceDictionary (Picard)]
- **variant-filtering**: reduce the number of false-positive variant calls
  - [create-somatic-panel-of-normals][create-somatic-panel-of-normals]: wrapper for [CreateSomaticPanelOfNormals][CreateSomaticPanelOfNormals]
- **variant-manipulation**: deal with VCF files.
  - [select-variants][select-variants]: wrapper for [SelectVariants][SelectVariants]


[create-read-count-panel-of-normals]: [gatk/cnv/create-read-count-panel-of-normals]
[denoise-read-counts]: [gatk/cnv/denoise-read-counts]
[collect-read-counts]: [gatk/coverage/collect-read-counts]
[get-pileup-summaries]: [gatk/coverage/get-pileup-summaries]
[preprocess-intervals]: [gatk/intervals/preprocess-intervals]
[index-feature-file]: [gatk/misc/index-feature-file]
[mutect2]: [gatk/mutect2]
[tumor-normal]: [gatk/mutect2/tumor-normal]
[tumor-only]: [gatk/mutect2/tumor-only]
[mark-duplicates]: [gatk/preprocessing/mark-duplicates]
[base-recalibrator]: [gatk/preprocessing/base-recalibrator]
[apply-bqsr]: [gatk/preprocessing/apply-bqsr]
[calculate-contamination]: [gatk/qc/calculate-contamination]
[create-sequence-dictionary]: [gatk/reference/create-sequence-dictionary]
[create-somatic-panel-of-normals]: [gatk/variant-filtering/create-somatic-panel-of-normals]
[select-variants]: [gatk/variant-manipulation/select-variants]

[CreateReadCountPanelOfNormals]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_CreateReadCountPanelOfNormals.php]
[DenoiseReadCounts]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_DenoiseReadCounts.php]
[CollectReadCounts]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_CollectReadCounts.php]
[GetPileupSummaries]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_contamination_GetPileupSummaries.php]
[PreprocessIntervals]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_PreprocessIntervals.php]
[PreprocessIntervals]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_copynumber_PreprocessIntervals.php]
[IndexFeatureFile]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.3.0/org_broadinstitute_hellbender_tools_IndexFeatureFile.php]
[Mutect2 with tumor & normal sample]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_mutect_Mutect2.php]
[Mutect2 with single sample]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_mutect_Mutect2.php]
[MarkDuplicates]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.4.0/picard_sam_markduplicates_MarkDuplicates.php]
[BaseRecalibrator]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_BaseRecalibrator.php]
[ApplyBQSR]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_ApplyBQSR.php]
[CalculateContamination]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_contamination_CalculateContamination.php]
[CreateSequenceDictionary (Picard)]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/4.0.3.0/picard_sam_CreateSequenceDictionary.php]
[CreateSomaticPanelOfNormals]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_mutect_CreateSomaticPanelOfNormals.php]
[SelectVariants]: [https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_variantutils_SelectVariants.php]
