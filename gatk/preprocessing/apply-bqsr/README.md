# ApplyBQSR ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_bqsr_ApplyBQSR.php))

apply base quality score recalibration.

## IO

- *{sample}*.bam, *{reference}*.fasta, recalibrated_data.table -> *{sample}*.recalibrated.bam

## Exmaple snakemake rules
```python
rule mark_duplicates:
    input:
        bam = '{sample}.bam',
        reference = '{reference}.fasta',
        recalibration_table = '{sample}_recalibration.table',
    output:
        '{sample}.recalibrated.bam'
    params:
        # Optional parameters. Omit if unused.
        java_options = '-Xmx32g'
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/preprocessing/apply-bqsr'

```
