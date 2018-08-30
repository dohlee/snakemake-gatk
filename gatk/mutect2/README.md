# Mutect2 ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_mutect_Mutect2.php))

call somatic SNPs and indels.

## Note

This wrapper is largely inspired by [this wonderful tutorial on Mutect2](https://gatkforums.broadinstitute.org/gatk/discussion/11136).

## IO

- [Tumor-only](tumor-only/) (usually used to create PoN)
  - *{sample}*.bam, reference -> *{sample}*.vcf.gz
- [Tumor-normal](tumor-normal/)
  - *{tumor_sample}*.bam, *{normal_sample}*.bam, reference -> *{tumor_sample}*.vcf.gz

## Wrappers for possible use cases

1. [mutect2/tumor-normal](tumor-normal/)
2. [mutect2/tumor-only](tumor-only/)
