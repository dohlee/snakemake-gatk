# GetPileupSummaries ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_contamination_GetPileupSummaries.php))

get pileup metrics as a table, which is used to infer contamination.

## IO

- *{sample}*.bam, *{common_biallelic_variants}*.vcf.gz (can be obtained by using SelectVariants with option `--restrict-alleles-to BIALLELIC`) -> *{sample}*.pileupsummaries.table

## Example snakemake rules

```python
rule get_pileup_summaries:
    input:
        # Required arguments.
        bam = '{sample}.bam',
        common_biallelic_variants = 'resources/small_exac_common_3.hg38.vcf.gz'
        # Optional arguments. Omit unused files.
    output:
        '{sample}.pileupsummaries.table'
    params:
        java_options = '-Xmx4g',
        extra = '',
    threads: 1
    resources: RAM = 4
    logs: 'logs/gatk/get-pileup-summaries/{sample}.log'
    wrapper:
        'http://dohlee-bio.info:9193/gatk/coverage/get-pileup-summaries'
```
