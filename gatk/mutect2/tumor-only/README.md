# Mutect2/tumor-normal ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_mutect_Mutect2.php))

call somatic SNPs and indels with a single sample.

## Note

This wrapper is largely inspired by [this wonderful tutorial on Mutect2](https://gatkforums.broadinstitute.org/gatk/discussion/11136).

## IO

- *{sample}*.bam, reference -> *{sample}*.vcf.gz

## Example snakemake rules

```python
rule mutect2_tumor_only:
    input:
        # Required arguments.
        reference = 'reference/Homo_sapiens_assembly38.fasta',
        bam = '{sample}.bam',
        bam_idx = '{sample}.bam.bai',
        reference_dict = 'reference/Homo_sapiens_assembly38.dict'
        # Optional arguments. Omit unused files.
    output:
        '{sample}.vcf.gz'
    params:
        extra = '--disable-read-filter MateOnSameContigOrNoMappedMateReadFilter '
    threads: 1
    log: 'logs/gatk/mutect2-tumor-only/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/mutect2/tumor-only'
```
